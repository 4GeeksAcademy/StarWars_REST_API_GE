import React,{useContext, useEffect} from "react";
import { Context } from "../store/appContext";
import { useParams } from "react-router-dom";

export const DetailCharacter = () => {
    const {store,actions} = useContext(Context);
    const params = useParams();
    useEffect(() => {
        actions.oneCharacters(params.id) 
    },[])
    console.log(store.character)

    return(
        <div className="container">
            <h1 style={{color: "red"}}>Character:</h1>
            <div className="card mb-3" style={{maxWidth: "540px"}}>
                <div className="row g-0">
                    <div className="col-md-4">
                    <img src={`https://starwars-visualguide.com/assets/img/characters/${params.id}.jpg`} className="card-img-top" alt="..." />
                    </div>
                    <div className="col-md-8" >
                        <div className="card-body">
                            <h5 className="card-title">{store.character.properties?.name}</h5>
                            <p className="card-text"><strong>Height:</strong> {store.character.properties?.height}</p>
                            <p className="card-text"><strong>Eye Color:</strong> {store.character.properties?.eye_color}</p>
                            <p className="card-text"><strong>Birt Year:</strong> {store.character.properties?.birth_year}</p>
                            <p className="card-text"><strong>Hair Color:</strong> {store.character.properties?.hair_color}</p>
                        </div>
                    </div>
                </div>
            </div>
        
        </div>
    )
};
