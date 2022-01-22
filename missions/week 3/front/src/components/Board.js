import React,{useState, useEffect} from 'react';
import {Link, useHistory} from 'react-router-dom';
import '../css/main.css';
import axios from 'axios';

function Board(props) {

    const history = useHistory();

    const [productList, setProductList] = useState([]);

    useEffect(() => {
        const take = async () => {
            const {data} = await axios.get('http://127.0.0.1:8000/product/')

            ;
            setProductList(data);
        };
        take();
    }, []);

    const Deleteproduct = async (product_id)=> {
        if(props.user.length!==0) {
            if (window.confirm('정말 삭제하시겠습니까 ?') === true) {
                await axios.delete('http://localhost:8000/product/delete/' + product_id + '/', {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`,
                    }
                }).then(history.push('/'))
                    .then(history.go(0));
            }
        }else {
            alert("권한이 없습니다.")
        }
    };



    const renderProducts = productList.map((product) => <li key={product.id} className="cell">
                                                            <div className="img-box ">
                                                                <img src={`http://localhost:8000/${product.image}/`} />
                                                            </div>
                                                            <div>{product.name}</div>
                                                            <div>{product.price}</div>
                                                            <button className="upButton" onClick={(e)=>{Deleteproduct(product.id, e)}}>삭제하기</button>
                                                        </li>);
    return (
        <div >
            <div className="list-box-1 con">
                <ul className="row">{renderProducts}</ul>


            </div>

        </div>
    );
}

export default Board;