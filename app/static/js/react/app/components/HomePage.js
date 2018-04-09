import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';

class HomePage extends React.Component {
  render() {
    return (
      <h1>FloSports Coffee Connection</h1>
    )
  }
}

HomePage.propTypes = {
  filter: PropTypes.string,
  onFilter: PropTypes.func
};

const mapStateToProps = (state) => {
  return {
    filter: state.filter
  };
};


export default connect(
  mapStateToProps,
)(HomePage);
