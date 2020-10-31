const { protocol , session, app, BrowserWindow } = require('electron')
const util = require('util')
const Store = require('electron-store');
const { exec } = require('child_process');
const store = new Store()

 // where public folder on the root dir

function getUrl(secure, domain){
    const scheme = secure ? "https" : "http";
    const host = domain[0] === "." ? domain.substr(1) : domain;
    return scheme + "://" + host;
}

function createWindow() {
    // Load cookies from persistent storage
    try{
        cks = store.get("cookies")
        cks.forEach(element => {
            // Set url for cookie
            element.url = getUrl(element.secure, element.domain)

            session.defaultSession.cookies.set(element)
                .then(() => {
                   //
                }, (error) => {
                    console.error(error)
                })
        })
        console.log("All cookies set!")
    } catch (err) {
        console.log("No cookies set yet!")
    }
    
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            enableRemoteModule: true, // For Electron-Storage to work properly
            nodeIntegration: true,
            webviewTag: true, // To use webview tags
            // Following two options are required to make sure iframes load properly
            nodeIntegrationInSubFrames: true,
            sandbox: true
        }
    })

    // win.loadFile('index.html')
    win.loadURL('https://collab.its.virginia.edu/portal')
    // win.webContents.openDevTools()
}

// app.on('session-created', (session) => {
//     console.log(session)
// })

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
    session.defaultSession.cookies.get({})
        .then((cookies) => {
            store.set("cookies", cookies)
            // console.log(store.get("cookies"))
        }).catch((error) => {
            console.log(error)
        })
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow()
    }
})
