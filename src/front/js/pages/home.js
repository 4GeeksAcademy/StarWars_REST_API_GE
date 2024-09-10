import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

import { CardCharacter } from "../component/CardCharacters";
import { Planets } from "../component/Planets";
import { Vehicles } from "../component/Vehicles";

export const Home = () => {
	const { store, actions } = useContext(Context);
	return (
		<div className="container" style={{background: "black"}}>
		<CardCharacter/>
		<Planets/>
		<Vehicles/>
	</div>
	);
};
