<h1>MemeMan.Me</h1>
<p>Simple, put your face or any face on mememan :)</p>
<p>Link to website: [Not live yet]</p>
<p>Link to API to be use in your porjects: [Not live yet]</p>

<h1>API Documentation</h1>

<p>Send all request to /API/upload <b>Note</b>: The API does have CORS turn on</p>
<p><b>Important</b>: Send base64 string as a normal string (don't remove data:image/[image-type];base64). It takes a couple of seconds for the image to be process by the server and be sent back to the client</p>

<h2>Examples of Getting and Requesting Data</h2>
<br>
    <span><b>Example of client request:</b></span>
    <pre>
        <code>
            //Send request as json 
            {   
                data: [base64-string-image]
            } 
        </code>
    </pre>
<br>
    <span><b>Example of result after sending request:</b></span>
    <pre>
        <code>
            ///This is also a json object
            {   
                img: [base64-string-image] 
            } 
        </code>
    </pre>
<br>
<span><b>Example of result if an ERROR has happen:</b></span>
    <pre>
        <code>
            //This is also a json object
            {  
                img: "fail" 
            } 
        </code>
    </pre>
<br>

<h1>Contact Info</h1>
    <span>Reddit: <a href="https://www.reddit.com/user/Guuzzeji">/u/Guuzzeji</a></span><br>
    <span>Discord: @Guuzzeji#2245</span><br>
    <span>Github: <a href="https://github.com/Guuzzeji">@Guuzzeji</a></span>
