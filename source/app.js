import React, { useCallback, useEffect } from "react";
import ReactDOM from "react-dom";
import { createRoot } from 'react-dom/client';

const userDisease = createRoot(document.getElementById("userDisease"));
const userAllergy = createRoot(document.getElementById("userAllergy"));
const userReligion = createRoot(document.getElementById("userReligion"));
const myButton = createRoot(document.getElementById("myButton"));

function AddDiseaseOptions() {
    return <>
        <option>없음</option>
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
        <option>없음</option>
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
        <option>없음</option>
        <option>이슬람교</option>
        <option>유대교</option>
        <option>불교</option>
        <option>제칠일안식일예수재림교</option>
        <option>시크교</option>
    </>;
}

function Geolocation_Callback(position) {
    window.alert(position.coords.latitude + ' ' + position.coords.longitude);
}

function MyButton() {
    const handleOnClick = (e) => {
        e.preventDefault();
        navigator.geolocation.getCurrentPosition(Geolocation_Callback);
    }

    return <button className="btn btn-primary" onClick={handleOnClick}>추천받기</button>;
}

userDisease.render(<AddDiseaseOptions />);
userAllergy.render(<AddAllergyOptions />);
userReligion.render(<AddReligionOptions />);
myButton.render(<MyButton />);