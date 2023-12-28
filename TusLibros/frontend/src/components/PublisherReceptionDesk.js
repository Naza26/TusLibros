import React, {Component} from "react";
import PropTypes from "prop-types";
import Container from "@mui/material/Container";
import BookRack from "./BookRack";
import Drawer from "@mui/material/Drawer";
import Header from "./Header";
import Cart from "./Cart";
import CallToTakeACart from "./CallToTakeACart";
import {Alert, Snackbar} from "@mui/material";


export default class PublisherReceptionDesk extends Component {

    static propTypes = {
        app: PropTypes.object.isRequired
    };

    constructor(props) {
        super(props);
        this.state = {
            showCart: false,
            cart: null,
            message: null
        }
    }

    render() {
        return <>
            {this.renderHeader()}
            {this.renderMainContent()}
            {this.renderMessage()}
        </>
    }

    renderHeader() {
        return <Header onActionDo={() => this._listCart()} cartSize={this._cartSize()}/>;
    }

    renderMainContent() {
        return <main>
            {this.renderCallToTakeACart()}
            {this.renderCartPanel()}
            <Container sx={{py: 8}} maxWidth="md">
                <BookRack app={this.props.app} onAddToCartDo={ (aBook) => this._addToCart(aBook)}/>
            </Container>
        </main>;
    }

    renderCallToTakeACart() {
        return <CallToTakeACart onActionDo={() => this._takeACart()}/>
    }

    renderCartPanel() {
        return <Drawer
            anchor={'right'}
            open={this.state.showCart}
            onClose={() => this.setState({showCart: false})}
        >
            {this.renderCart()}
        </Drawer>
    }

    renderCart() {
        return <Cart cart={this.state.cart}/>;
    }

    renderMessage(){
        if (this.state.message != null) {
            return <Snackbar open={true} autoHideDuration={6000} onClose={() => this._closeMessage()}>
                <Alert severity={this.state.message.severity} sx={{width: '100%'}}>
                    {this.state.message.text}
                </Alert>
            </Snackbar>
        }
    }

    _listCart() {
        this._fillCartWithItems(this._cart().id, true);
    }

    _takeACart() {
        const result = this.props.app.createCart();
        this._handlePromisedResult(result, (aSuccessfulResponse) => {
            this.setState({cart: {id: aSuccessfulResponse.cartId(), items: []}, showCart: false})
            this._notifyMessageWith(
                "success", "Ya puedes agregar tus libros preferidos al carrito")
        })
    }

    _fillCartWithItems(cartId, showCart) {
        const result = this.props.app.listCart(cartId);
        this._handlePromisedResult(result, (aSuccessfulResponse) => {
            this.setState({cart: {id: cartId, items: this._itemsFrom(aSuccessfulResponse)}, showCart: showCart})
        })
    }

    _itemsFrom(response) {
        return response.cartItemsCollect((isbn, quantity) => {
            const aBook = this.props.app.books().find( (each) => each.isbn === isbn );
            return {article: aBook, quantity: quantity}
        });
    }

    _addToCart(aBook) {
        const result = this.props.app.addToCart(aBook, this._cart());
        this._handlePromisedResult(result, (aSuccessfulResponse) => {
            this._notifyMessageWith("success", `Se ha agregado "${aBook.title}" al carrito!`)
        })
    }

    _handlePromisedResult(aPromisedResult, aClosureForSuccessfulResponse) {
        aPromisedResult.then((response) => {
            if (response.hasError()) {
                this._notifyMessageWith("error", response.message())
            } else {
                return aClosureForSuccessfulResponse(response)
            }
        })
    }

    _hasTakenACart() {
        return this.state.cart != null;
    }

    _closeMessage() {
        this.setState({message: null});
    }

    _notifyMessageWith(severity, text) {
        this.setState({message: {severity: severity, text: text}});
    }

    _cart() {
        if (!this._hasTakenACart()) {
            return {id: '', items: []};
        } else {
            return this.state.cart;
        }
    }

    _cartSize() {
        return this._cart().items.length
    }
}