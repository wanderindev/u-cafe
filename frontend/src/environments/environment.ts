export const environment = {
    production: false,
    apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
    auth0: {
        url: 'dev-u-cafe', // the auth0 domain prefix
        audience: 'u-cafe', // the audience set for the auth0 app
        clientId: '0TCOG2XxpFWolY3kbtd1qRTHAGjPV3Gs', // the client id generated for the auth0 app
        callbackURL: 'http://127.0.0.1:8100', // the base url of the running ionic application.
    }
};
