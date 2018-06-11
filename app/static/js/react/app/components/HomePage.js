import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import WelcomeInfo from "./WelcomeInfo";

class HomePage extends React.Component {
  render() {
    return (
      <div>
        <h1>FloSports Coffee Connection</h1>
        <WelcomeInfo/>
      </div>
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
