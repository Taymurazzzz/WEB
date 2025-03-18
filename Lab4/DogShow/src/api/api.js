import axios from "axios";
const api = axios.create({
baseURL: "http://localhost:8000/api/",
headers: {
    "Content-Type": 'application/json'
}
})

const auth = axios.create({
baseURL: "http://localhost:8000/auth/",
headers: {
    "Content-Type": 'application/json'
}
})


export const getShows = async () => {
try {
    const response = await api.get("shows/");
    return response.data.results;
} catch (e) {
    console.error("Ошибка при получении выставок:", e);
    throw e;
}
};
export const getShowsById = async (id) => {
    try {
        const response = await api.get(`shows/${id}/`);
        console.log(response.data)
        return response.data;
    } catch (e) {
        console.error("Ошибка при получении выставок:", e);
        throw e;
    }
    };

export const regUser = async (userData) => {
    try {
      const response = await auth.post("users/", userData);
      return response;
    } catch (e) {
      console.error("Ошибка при регистрации пользователя:", e);
      throw e;
    }
  };

  export const userInfo = async () => {
    try {
        const token = localStorage.getItem("token");
        const response = await auth.get("users/me/", {headers: {
            "Authorization": `Token ${token}`
        }});
  
        const id = response.data.id;
    
        const info = await api.get(`users/${id}/`);
    
        return info.data;
    } catch (e) {
        console.error("Ошибка при получении информации о пользователе:", e);
        throw e;
    }
  };

export const loginUser = async(params) => {
try{
    const json = JSON.stringify(params)
    console.log(params)
    const data = await auth.post("token/login/", json)
    const token = data.data.auth_token
    console.log(token)
    localStorage.setItem("token", token)
    return data.status
} catch(e){
    throw e
}

}

export const getDog = async(userId) => {
    try{
        const response = await api.get("dogs/")
        const dogs = response.data.results.filter(dog => dog.owner === userId)
        console.log(dogs)
        return dogs
    }catch(e){
        throw e
    }
}

export const createDog = async(dogData) => {
    try{
        const token = localStorage.getItem("token");
        const response = await api.post("dogs/", dogData, {headers: {
            "Authorization": `Token ${token}`
        }})
    }catch(e){
        throw e
    }
}

export const regDog = async(dogData) => {
    try{
        const token = localStorage.getItem("token");
        const response = await api.post("participating-dogs/", dogData, {headers: {
            "Authorization": `Token ${token}`
        }})
    }catch(e){
        throw e
    }
}

