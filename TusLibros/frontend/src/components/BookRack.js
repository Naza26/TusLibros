import React, {Component} from "react";
import PropTypes from "prop-types";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import CardMedia from "@mui/material/CardMedia";
import CardContent from "@mui/material/CardContent";
import CardActions from "@mui/material/CardActions";
import {IconButton, Rating} from "@mui/material";
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';
import Stack from "@mui/material/Stack";
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';


export default class BookRack extends Component {

    static propTypes = {
        app: PropTypes.object.isRequired,
        onAddToCartDo: PropTypes.func.isRequired,
    };

    constructor(props) {
        super(props);
        this._books = this.props.app.books()
    }

    render() {
        return <Grid container spacing={4}>
            {this._books.map((aBook) => (
                <Grid item key={aBook.isbn} xs={12} sm={6} md={4}>
                    {this.renderBook(aBook)}
                </Grid>
            ))}
        </Grid>
    }

    renderBook(aBook) {
        return <Card sx={{height: '100%', display: 'flex', flexDirection: 'column'}}>
            {this.renderBookCoverOf(aBook)}
            {this.renderBookDetailOf(aBook)}
            {this.renderBookActionsOn(aBook)}
        </Card>;
    }

    renderBookCoverOf(aBook) {
        return <CardMedia
            component="div"
            sx={{pt: '56.25%'}}
            image={aBook.cover}
        />;
    }

    renderBookDetailOf(aBook) {
        return <CardContent sx={{flexGrow: 1}}>
            <Typography gutterBottom variant="h5">
                {aBook.title}
            </Typography>
            <Typography>
                {aBook.description.slice(0, 100) + "..."}
            </Typography>
            <Rating value={aBook.score} precision={0.5} readOnly/>
        </CardContent>;
    }

    renderBookActionsOn(aBook) {
        return <CardActions>
            <Stack direction="row" justifyContent="space-around" alignItems="center" sx={{width: '100%'}}>
                {this.renderAddToCartBar(aBook)}
                {this.renderPriceOf(aBook)}
            </Stack>
        </CardActions>;
    }

    renderPriceOf(aBook) {
        return <Stack direction="row" justifyContent="flex-end" alignItems="center">
            <AttachMoneyIcon fontSize="small"/>
            <Typography variant="h6">{aBook.price}</Typography>
        </Stack>;
    }

    renderAddToCartBar(aBook) {
        return <IconButton
            color="primary" title="Agregar al carrito"
            onClick={() => {
                this.props.onAddToCartDo(aBook)
            }}>
            <AddShoppingCartIcon/>
        </IconButton>;
    }
}