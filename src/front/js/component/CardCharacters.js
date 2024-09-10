import React, {useEffect, useState, useContext, useSyncExternalStore} from "react";
import { Link } from "react-router-dom";
import {Context} from "../store/appContext"


export const CardCharacter = () => {
    const {store, actions} = useContext(Context);

    
    
    useEffect (()=>{
        actions.getCharacters();
    },[])
    
    console.log(store.characters)
	return (
        <div >
            <h1 style={{color: "red"}}>Character:</h1>
            <div className="row row-cols-1 row-cols-md-4 mb-3 text-center">
                {store.characters.map((item,index)=>{
                    return(
                        <div className="card p-4 m-3" key={index}>
                            <div className="card" >
                                <img src={`https://starwars-visualguide.com/assets/img/characters/${item.uid}.jpg`} className="card-img-top" alt="..." />
                                <div className="card-body md-col3">
                                        <h5 className="card-title">{item.name}</h5>
                                        <div className="d-flex justify-content-between">
                                            <Link to={`/detailCharacter/${item.uid}`} className="btn  btn-light btn-outline-primary">Learn more!</Link>
                                        <button className="btn btn-light btn-outline-warning btn-bg-white" onClick={()=>{actions.addFavorites(item.name)}} ><i className="far fa-heart border-0" /></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )
                })}
            </div>
        </div>
	);
};
