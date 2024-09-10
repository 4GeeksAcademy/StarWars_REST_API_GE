const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			entra : "",
			count : 0,
			characters:[],
			charactersBack:[],
			planets:[],
			vehicles:[],
			character:{},
			planet:{},
			vehicle:{},
			fav:[],
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			]
		},
		actions: {
			// Use getActions to call a function within a fuction
			fetchWithCheck: async (url, options = {}) => {
                try {
                    const response = await fetch(url, options);
                    const contentType = response.headers.get("content-type");
                    if (!response.ok) {
                        if (contentType && contentType.includes("application/json")) {
                            const errorData = await response.json();
                            throw new Error(JSON.stringify(errorData));
                        } else {
                            throw new Error("Error in fetch: Non-JSON response received");
                        }
                    }
                    return contentType && contentType.includes("application/json")
                        ? await response.json()
                        : null;
                } catch (error) {
                    console.error("Error in fetch:", error.message);
                    return null;
                }
            },
			prueba: async (uid, name) => {
				const response = await getActions().fetchWithCheck(`https://www.swapi.tech/api/people/${uid}`);
				if (response) {
					const store = getStore();
					const Character =  response.result.properties;
					const properties = store.charactersBack;
					const newproperties = [...properties,{Character, uid, name}]
					setStore({charactersBack:newproperties})
					
					console.log("************** ENTRE A PRUEBA!!!! RESPONSE", getStore().charactersBack);
					
					return true;
				}
				return false;
			},
			getCharacters: async () => {
				const response = await getActions().fetchWithCheck("https://www.swapi.tech/api/people");
					if (response) {
						setStore({characters:response.results});
						const data = getStore().characters;
						{data.map(async(item,index)=>{
							const nada =  await getActions().prueba(item.uid, item.name);
							getStore().count = getStore().count + 1;
						})}
						return getStore().count;
					}
					else{
						return false;

					}
			},
			
			getPlanets: () => {
				fetch("https://www.swapi.tech/api/planets")
				.then(res => res.json())
				.then(data => setStore({planets:data.results}))
				.catch(err => console.error(err))
			},
			getVehicles: () => {
				fetch("https://www.swapi.tech/api/vehicles")
				.then(res => res.json())
				.then(data => setStore({vehicles:data.results}))
				.catch(err => console.error(err))
			},
			oneCharacters: (id) => {
				fetch(`https://www.swapi.tech/api/people/${id}`)
				.then(res => res.json())
				.then(data => setStore({character:data.result}))
				.catch(err => console.error(err))
			},
			onePlanet: (id) => {
				fetch(`https://www.swapi.tech/api/planets/${id}`)
				.then(res => res.json())
				.then(data => setStore({planet:data.result}))
				.catch(err => console.error(err))
			},	
			oneVehicle: (id) => {
				fetch(`https://www.swapi.tech/api/vehicles/${id}`)
				.then(res => res.json())
				.then(data => setStore({vehicle:data.result}))
				.catch(err => console.error(err))
			},
			addFavorites(item){
				const store = getStore()
				const favorites = store.fav
				const newFavorites = [...favorites,{name:item,id:favorites.length}]
				setStore({fav:newFavorites})
			},
			deleteFavorites(id){
				const store = getStore()
				const favorites = store.fav
				const editFavorites = favorites.filter((item)=>item.id !== id)
				setStore({fav:editFavorites})
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
