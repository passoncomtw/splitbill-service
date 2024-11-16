const passport = require('passport');
const passportJWT = require('passport-jwt');
const isEmpty = require('lodash/isEmpty');
const LocalStrategy = require('passport-local').Strategy;
const { getUserWithPasswordResult } = require("../services/userServices");

const { saltHashPassword } = require('./utils');

const JWTStrategy = passportJWT.Strategy;
const ExtractJWT = passportJWT.ExtractJwt;

const { AUTH_SECRET } = process.env;

const validateTransactionCode = (user, transactionCode) => {
  const hashTransactionCode = saltHashPassword(transactionCode);

  return user.transactionCode === hashTransactionCode;
};

const validateUserAndPassword = (user, password) => {
  if (isEmpty(user)) return { validated: false };

  const hashPassword = saltHashPassword(`${user.account}${password}`);
  if (hashPassword !== user.password) return { validated: false };

  return { validated: true };
};

passport.use(
  'app-user',
  new LocalStrategy(
    {
      usernameField: 'token',
      passwordField: 'password',
    },
    async (token, password, done) => {
      const userResult = await axios
      return done(null, user);
    }
  )
);

passport.use(
  new JWTStrategy(
    {
      jwtFromRequest: ExtractJWT.fromAuthHeaderAsBearerToken(),
      secretOrKey: AUTH_SECRET,
    },
    function (jwtPayload, done) {
      done(null, jwtPayload, { message: 'Logged In Successfully' });
    }
  )
);

//Todo: 新增 session
passport.serializeUser((user, done) => {
  done(null, user);
});
//Todo: 移除 session
passport.deserializeUser((user, done) => {
  done(null, user);
});

module.exports.jwtAuthorizationMiddleware = (req, res, next) => {
  passport.authenticate('jwt', { session: true }, (err, user, info) => {
    if (err || !user) {
      const err = {
        success: false,
        data: {
          message: info.message,
        },
      };

      return res.status(401).json(err); // send the error response to client
    }

    req.user = user;

    return next();
  })(req, res, next);
};

module.exports.validateTransactionCode = validateTransactionCode;
