import React,{useContext} from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";


export const Navbar = () => {
	const {store,actions} = useContext(Context)
	console.log(store.fav)
	return (
		<nav className="navbar bg-dark margin-left">
			<Link to="/">
				<img src="https://img.icons8.com/ios/50/000000/star-wars.png" className="card-img-top" alt="..."/>	
			</Link>
			<div className="ml-auto">
				<div className="dropdown">
					<button className="btn btn-light btn-outline-primary btn-bg-white dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false"  >
						Favorites {store.fav.length}
					</button>
					<ul className="dropdown-menu " >
						{store.fav.map((item,index)=>{
							return <li key={index}><a className="dropdown-item" href="#">{item.name} <span onClick={()=>{actions.deleteFavorites(item.id)}}><i className="trash fas fa-trash-alt" /></span></a></li>
							}
							)
						}
							
					</ul>
				</div>
			</div>
		</nav>
	);
};
