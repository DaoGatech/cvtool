import Canvas from './Canvas.react';
import React from 'react';

class Application extends React.Component {

  render() {
    return (
      <div className="container-fluid">
        <div className="row">
          <div className="col-md-4 text-center">
          	<Canvas />
          </div>
        </div>
      </div>
    );
  }
}

module.exports = Application;