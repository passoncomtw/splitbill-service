import jwt from "jsonwebtoken";
import isEmpty from "lodash/isEmpty";
import pick from "lodash/pick";
import passport from "passport";
import { responseErrWithMsg, responseOk } from "~/helpers/response";
import { lineSigninRequestSchema } from "~/helpers/schemas";
import { parseUserResponse } from "~/services/userServices";

const { AUTH_SECRET } = process.env;

/**
 * @typedef LineLoginRequest
 * @property {string} token.required
 *   - LIFF 的 id token
 *   - eg: eyJraWQiOiIwZjdhYzBmOGEyMmUxMzFiNWZlNzVhOWNlMTY5OWFjYTE1MGY3ZjZjMGVkNzVlMjgyYjNiZjdmYjA5N2E3NjNlIiwidHlwIjoiSldUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2FjY2Vzcy5saW5lLm1lIiwic3ViIjoiVTlhMTI4YWFjMTU0ZGYxNmU4YmIyMzc4MjJjODMwOTBjIiwiYXVkIjoiMjAwNjIxMDgxNyIsImV4cCI6MTczMTcyNDA5MSwiaWF0IjoxNzMxNzIwNDkxLCJhbXIiOlsibGluZXNzbyJdLCJuYW1lIjoiVG9tYXMgTGluIO-jvyIsInBpY3R1cmUiOiJodHRwczovL3Byb2ZpbGUubGluZS1zY2RuLm5ldC8waEtRT25iQWhORkg1eUZ3Y2lxUUpyS1U1U0doTUZPUkkyQ25OU1NBSVRTVVlNSVZVZ0hDSU1TZ0lRU2tjS0lsRjlTQ05aRUZaRkdVeGYiLCJlbWFpbCI6ImhvcnNla2l0MTk4MkBnbWFpbC5jb20ifQ.zmp86XzmTkYxmAC9Im_oOZ7402ZAI6QKgLtcAixq6Eh_LVhtMcriBMklhcGVyLCylWoEL_--I1KKSkEK4rFscg
 */

/**
 * @typedef MemberInformation
 * @property {number} id.required
 *  - member Id
 *  - eg: 1
 * @property {string} name.required
 *  - member name
 *  - eg: testdemo001
 */

/**
 * @typedef LoginResponse
 * @property {[string]} token.required - JWT token string
 * @property {MemberInformation.model} user.required - member information
 */

/**
 * Line LogIn API.
 * @group AppAuthorization
 * @route POST /auth/line
 * @param {LineLoginRequest.model} data.body.required - the new point
 * @returns {LoginResponse.model} 200 - success, return requested data
 * @returns {String} 400 - invalid request params/query/body
 * @returns {String} 404 - required data not found
 * @returns {Error} 500 - unexpected error
 * @security none
 * @typedef LoginResponse
 * @property {{integer}} code - response code - eg: 200
 */
export const lineLoginRoute = async (req, res) => {
  try {
    await lineSigninRequestSchema.validate(req.body);
  } catch (error) {
    return responseErrWithMsg(res, error.message);
  }

  passport.authenticate("app-user", { session: false }, async (error, user) => {
    try {
      if (error) throw error;
      if (isEmpty(user)) {
        throw new Error("使用者不存在");
      }
      // const expireIn = add(new Date(), { days: 1 }).getTime();

      const signInfo = pick(user, ["id", "phone", "name"]);
      const token = jwt.sign(
        {
          data: signInfo,
          // exp: expireIn,
        },
        AUTH_SECRET
      );

      return responseOk(res, {
        token,
        user: parseUserResponse(user),
      });
    } catch (error) {
      responseErrWithMsg(res, error.message);
    }
  })(req, res);
};


// /**
//  * @typedef LoginRequest
//  * @property {string} phone.required
//  *   - auth0 Response.sub
//  *   - eg: 0987654321
//  * @property {string} password.required
//  *   - password: 6 ~ 20 個英數組合
//  *   - eg: a12345678
//  */

// /**
//  * @typedef MemberInformation
//  * @property {number} id.required
//  *  - member Id
//  *  - eg: 1
//  * @property {string} phone.required
//  *  - member.phone
//  *  - eg: 0987654321
//  * @property {string} name.required
//  *  - member name
//  *  - eg: testdemo001
//  */

// /**
//  * @typedef LoginResponse
//  * @property {[string]} token.required - JWT token string
//  * @property {MemberInformation.model} user.required - member information
//  */

// /**
//  * LogIn API.
//  * @group AppAuthorization
//  * @route POST /app/login
//  * @param {LoginRequest.model} data.body.required - the new point
//  * @returns {LoginResponse.model} 200 - success, return requested data
//  * @returns {String} 400 - invalid request params/query/body
//  * @returns {String} 404 - required data not found
//  * @returns {Error} 500 - unexpected error
//  * @security none
//  * @typedef LoginResponse
//  * @property {{integer}} code - response code - eg: 200
//  */
// export const lineLoginRoute = async (req, res) => {
//   try {
//     await signinRequestSchema.validate(req.body);
//   } catch (error) {
//     return responseErrWithMsg(res, error.message);
//   }

//   passport.authenticate("app-user", { session: false }, async (error, user) => {
//     try {
//       if (error) throw error;
//       if (isEmpty(user)) {
//         throw new Error("使用者不存在");
//       }
//       // const expireIn = add(new Date(), { days: 1 }).getTime();

//       const signInfo = pick(user, ["id", "phone", "name"]);
//       const token = jwt.sign(
//         {
//           data: signInfo,
//           // exp: expireIn,
//         },
//         AUTH_SECRET
//       );

//       return responseOk(res, {
//         token,
//         user: parseUserResponse(user),
//       });
//     } catch (error) {
//       responseErrWithMsg(res, error.message);
//     }
//   })(req, res);
// };
