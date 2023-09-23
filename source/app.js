import React, { useCallback, useEffect } from "react";
import ReactDOM from "react-dom";
import { createRoot } from 'react-dom/client';
//import axios from "axios";

const root = createRoot(document.getElementById("root"));

class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state = {date: new Date()};
    }

    componentDidMount() {
        this.timerID = setInterval( () => this.tick(), 1000);
    }

    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    tick() {
        this.setState({
            date: new Date()
        });
    }

    render() {
        return (
            <div>
                <h1>Hello, world!</h1>
                <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
            </div>
        );
    }
}

function App() {
    /* useEffect(
        () => {
        axios.get('/api')
        .then((res)=>{Callback(res.data)})
        .catch((err)=>{console.log(err)})
        },[]
    );*/
    
    return (
        <div>
            <Clock />
            <Clock />
            <Clock />
        </div>
    );
}

root.render(<App />);