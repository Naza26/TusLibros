import {ApiClient} from "../../lib/communication/src";
import {ListCartEndpoint} from "./ListCartEndpoint";
import {CreateCartEndpoint} from "./CreateCartEndpoint";
import {AddToCartEndpoint} from "./AddToCartEndpoint";


export class TusLibrosRestInterface extends ApiClient {

    createCart() {
        const endpoint = new CreateCartEndpoint();
        return this._callEndpoint(endpoint, {});
    }

    listCart(aCartId){
        let values = {cartId: aCartId};
        const endpoint = new ListCartEndpoint();
        return this._callEndpoint(endpoint, values);
    }

    addToCart(aBook, aCart){
        let values = {bookIsbn: aBook.isbn, cartId: aCart.id};
        const endpoint = new AddToCartEndpoint();
        return this._callEndpoint(endpoint, values);
    }
}