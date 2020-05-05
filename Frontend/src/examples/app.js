import * as React from 'react';
import * as ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  NavLink,
  Redirect,
  Route,
  Switch,
} from 'react-router-dom';

import Graph from './Graph/graph';
import OutputSection from './OutputSection/output-section';
import InputSection from './InputSection/input-section';

import './app.scss';

class App extends React.Component {
  render() {
    return (
      <Router>
        <div>

          <div id="container">
            <InputSection />
            <Route exact={true} path="/" component={Graph} />
            <OutputSection />
          </div>
        </div>
      </Router>
    );
  }
}

if (typeof window !== 'undefined') {
  window.onload = () => {
    ReactDOM.render(<App />, document.getElementById('content'));
  };
}
