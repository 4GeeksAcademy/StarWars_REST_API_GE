import React,{useContext, useEffect} from "react";
import { Context } from "../store/appContext";
import { useParams } from "react-router-dom";

export const DetailPlanet = () => {
    const {store,actions} = useContext(Context);
    const params = useParams();
    useEffect(() => {
        actions.onePlanet(params.id) 
    },[])
    console.log(store.planet)

    return(
        <div className="container">
            <h1 style={{color: "red"}}>Planet:</h1>
            <div className="card mb-3" style={{maxWidth: "540px"}}>
                <div className="row g-0">
                    <div className="col-md-4">
                    <img src={`https://starwars-visualguide.com/assets/img/planets/${params.id}.jpg`} className="card-img-top" alt="..." />
                    </div>
                    <div className="col-md-8">
                    <div className="card-body">
                        <h5 className="card-title">{store.planet.properties?.name}</h5>
                        <p className="card-text"><strong>Diameter:</strong> {store.planet.properties?.diameter}</p>
                        <p className="card-text"><strong>Rotation Period:</strong> {store.planet.properties?.rotation_period}</p>
                        <p className="card-text"><strong>Population:</strong> {store.planet.properties?.population}</p>
                        <p className="card-text"><strong>Climate:</strong> {store.planet.properties?.climate}</p>
                        <p className="card-text"><strong>Terrain:</strong> {store.planet.properties?.terrain}</p>                        
                    </div>
                    </div>
                </div>
            </div>
        
        </div>
    )
};
