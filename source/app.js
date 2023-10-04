import React, { useCallback, useEffect } from "react";
import ReactDOM from "react-dom";
import { createRoot } from 'react-dom/client';

const root = createRoot(document.getElementById("root"));
// const userDataForm = createRoot(document.getElementById("ReactApp"));
// const recommandedFoodCards = createRoot(document.getElementById("FoodCards"));

function AddDiseaseOptions() {
    return <>
        <option>당뇨</option>
        <option>비만</option>
        <option>셀리악(Celiac)</option>
        <option>유당불내증</option>
        <option>고혈압</option>
        <option>신장 질환</option>
        <option>통풍</option>
        <option>심장 질환</option>
    </>;
}

function AddAllergyOptions() {
    return <>
        <option>알류</option>
        <option>참깨</option>
        <option>우유</option>
        <option>콩(대두)</option>
        <option>땅콩</option>
        <option>과일 및 채소</option>
        <option>견과류</option>
        <option>해산물 및 조개류</option>
        <option>밀</option>
    </>;
}

function AddReligionOptions() {
    return <>
        <option>이슬람교</option>
        <option>유대교</option>
        <option>불교</option>
        <option>제칠일안식일예수재림교</option>
        <option>시크교</option>
    </>;
}

function Geolocation_Callback(position) {
    window.alert(position.coords.latitude + ' ' + position.coords.longitude);
    document.getElementById("FoodCards").innerHTML=position.coords.latitude + ', ' + position.coords.longitude;
}

function MyButton() {
    const handleOnClick = (e) => {
        e.preventDefault();
        navigator.geolocation.getCurrentPosition(Geolocation_Callback);
    }

    return <button className="btn btn-primary w-25" onClick={handleOnClick}>추천받기</button>;
}

function CreateUserDataForm() {
    const HandleSubmit = (e) => {
        e.preventDefault();
        return;
    }

    return (
    <div className="container">
        <form id="userData" className="p-2 bg-secondary text-center" onSubmit={HandleSubmit}>
        <div className="row my-2">
            <div className="col">
                <h3>질병여부</h3>
                <select id="userDisease">
                    <option value="0">없음</option>
                    <AddDiseaseOptions />
                </select>
            </div>
            <div className="col">
                <h3>알러지 여부</h3>
                <select id="userAllergy">
                    <option value="0">없음</option>
                    <AddAllergyOptions />
                </select>
            </div>
            <div className="col">
                <h3>종교 여부</h3>
                <select id="userReligion">
                    <option value="0">없음</option>
                    <AddReligionOptions />
                </select>
            </div>
            <div className="col">
                <h3>비건 여부</h3>
                <select id="userVegan">
                <option>아니오</option>
                <option>예</option>
                </select>
            </div>
        </div>
        <div className="row justify-content-center">
            <MyButton />
        </div>
        </form>
    </div> );
}

function HandleFoodCards() {
    return <>
        <div id="FoodCards" className="vw-100 p-3 bg-info">test</div>
    </>;
}

function RenderRoot() {
    return <>
        <CreateUserDataForm />
        <HandleFoodCards />
    </>;
}

root.render(<RenderRoot />);

// userDataForm.render(<CreateUserDataForm />);
// recommandedFoodCards.render(<HandleFoodCards />);