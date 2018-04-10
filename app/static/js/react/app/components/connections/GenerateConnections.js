import PropTypes from 'prop-types';
import React from 'react';

export default class GenerateConnections extends React.Component {
  render() {
    return (
      <div>
        <button>Generate Connections</button>
      </div>
    )
  }
}

GenerateConnections.propTypes = {
  userID: PropTypes.string,
  userDetails: PropTypes.object
};

