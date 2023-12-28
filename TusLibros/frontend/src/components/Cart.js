import React, {Component} from "react";
import Typography from "@mui/material/Typography";
import {Avatar, Divider, List, ListItem, ListItemAvatar, ListItemText} from "@mui/material";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import PropTypes from "prop-types";


export default class Cart extends Component {

    static propTypes = {
        cart: PropTypes.object.isRequired
    };


    render() {
        return <Box
            sx={{
                bgcolor: 'background.paper',
                pt: 8,
                pb: 6,
            }}
        >
            <Container maxWidth="sm">
                {this.renterTitle()}
                {this.renderItems()}
            </Container>
        </Box>
    }

    renterTitle() {
        return <Typography
            variant="h5"
            align="center"
            color="text.secondary"
            gutterBottom
        >
            {this.title()}
        </Typography>;
    }

    title() {
        if (this.hasItems()) {
            return "¡Ya casi son tuyos!";
        }
        else {
            return "¡Comienza a armar tu pedido!"
        }
    }

    renderItems() {
        return <List sx={{width: '100%', maxWidth: 360, bgcolor: 'background.paper'}}>
                {this.props.cart.items.map((cartItem) => this.renderItem(cartItem))}
            </List>;
    }

    renderItem(cartItem) {
        return <>
            <ListItem alignItems="flex-start">
                <ListItemAvatar>
                    <Avatar src={cartItem.article.cover}/>
                </ListItemAvatar>
                <ListItemText
                    primary={cartItem.article.title}
                    secondary={
                        <>
                            <Typography
                                sx={{display: 'inline'}}
                                component="span"
                                variant="body2"
                                color="text.secondary"
                            >
                                {cartItem.quantity}
                            </Typography>
                        </>
                    }
                />
            </ListItem>
            <Divider variant="inset" component="li"/>
        </>;
    }

    hasItems() {
        return this.props.cart.items.length > 0;
    }
}