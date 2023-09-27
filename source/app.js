import React, { useCallback, useEffect } from "react";
import ReactDOM from "react-dom";
import { createRoot } from 'react-dom/client';

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

class Toggle extends React.Component {
    constructor(props) {
      super(props);
      this.state = {isToggleOn: true};
    }
  
    handleClick = () => {
      this.setState(prevState => ({
        isToggleOn: !prevState.isToggleOn
      }));
    }
  
    render() {
      return (
        <button onClick={this.handleClick}>
          {this.state.isToggleOn ? 'ON' : 'OFF'}
        </button>
      );
    }
}

class UserStatus extends React.Component {
    constructor(props) {
        super(props);
    }

    submit = () => {

    }

    render() {
        return (
            <>
                <div className="row row-cols-auto">
                        <div className="col">
                            <h3>질병여부</h3>
                            <select id="disease">
                                <option value="0">없음</option>
                            </select>
                        </div>
                        <div className="col">
                            <h3>알러지 여부</h3>
                            <select id="allergy">
                                <option value="0">없음</option>
                            </select>
                        </div>
                        <div className="col">
                            <h3>종교 여부</h3>
                            <select id="religion">
                                <option value="0">없음</option>
                            </select>
                        </div>
                        <div className="col">
                            <h3>비건이신가요?</h3>
                            <select id="allergy">
                                <option value="0">아니오</option>
                                <option value="1">예</option>
                            </select>
                        </div>
                </div>
                <div className="row">
                    <button className="button" onClick={this.submit}>추천받기</button>
                </div>
            </>
        )
    }
}

class CardsContainer extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
            </div>
        )
    }
}

class App extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
    }

    componentWillUnmount() {
    }

    render() {
        return (<>
            <UserStatus />
            <CardsContainer />
        </>)
    }
}

root.render(<App />);