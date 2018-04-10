import PropTypes from 'prop-types';
import React from 'react';

export default class GenerateConnections extends React.Component {
  onClickGenerateConnections() {
    // todo do fetch here to generate connections
    console.log('generator')
  }

  render() {
    return (
      <div>
        <button onClick={this.onClickGenerateConnections}>Generate Connections</button>
      </div>
    )
  }
}

GenerateConnections.propTypes = {
  userID: PropTypes.string,
  userDetails: PropTypes.object
};

