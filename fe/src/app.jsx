import React, { Component } from 'react';
import { Route, withRouter } from 'react-router';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Route
          exact
          path={'/'}
          component={() => <h1>Hello, CI</h1>}
        />
      </div>
    );
  }
}

export default App = withRouter(App);
