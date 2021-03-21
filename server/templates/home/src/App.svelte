<script>
	import { fade } from "svelte/transition";

	let fade_speed = 190;

	function uploadFile(e) {
		let filePath = e.target.files[0];

		const reader = new FileReader();

		reader.onload = function () {
			let view = document.getElementById("preview");
			view.src = reader.result;
			view.style.display = "block";
		};

		reader.readAsDataURL(e.target.files[0]);
		dis_preview = "display: black";
	}

	export let uploaded = false;
	export let result = null;
	export let dis_preview = "display: none";

	function uploadBtn() {
		uploaded = true;

		let body = {
			data: document.getElementById("preview").src,
		};

		fetch("/API/upload", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(body),
		})
			.then(function (res) {
				return res.json();
			})
			.then(function (data) {
				console.log(data);
				if (data.img != "fail") {
					result = data.img;
				} else {
					alert("Image has fail, please find another image");
					restart();
				}
			});
	}

	function restart() {
		uploaded = false;
		result = null;
		dis_preview = "display: none";
	}
</script>

<main>
	<center>
		<div class="header">
			<img id="icon" src="./emote-icon.jpg" alt="" />
			<h1>MemeMan.Me</h1>
			<img id="icon" src="./emote-icon.jpg" alt="" />
		</div>
		<span
			><i>Put Your Face On Mememan</i>
			<a href="/about">[ About ]</a></span
		>
		<hr />
		<br />
	</center>

	{#if result != null}
		<div
			in:fade={{ duration: fade_speed }}
			out:fade={{ duration: fade_speed }}
		>
			<img class="man-img" id="result" alt="" src={result} />
			<br />
			<br />
			<a download="mememanface" href={result}>Dowload Image</a>
			<span />
			<button
				style="background-color: #1DD3B0; color: white"
				on:click={restart}>Upload Again</button
			>
		</div>
	{/if}

	{#if uploaded == false && result == null}
		<div
			in:fade={{ duration: fade_speed }}
			out:fade={{ duration: fade_speed }}
			style="background-color:#fff; border-radius: 5px; padding: 10px;"
		>
			<center>
				<div style={dis_preview}>
					<img class="man-img" id="preview" alt="Fuck!" />
					<br />
				</div>
				<input type="file" on:change={uploadFile} accept="image/*" />
				<br />
				<button
					style="background-color: #1DD3B0; color: white"
					on:click={uploadBtn}>Upload Face</button
				>
			</center>
		</div>
	{:else if result == null}
		<center
			in:fade={{ duration: fade_speed }}
			out:fade={{ duration: fade_speed }}
		>
			<div class="loader" />
			<br />
			<span>Processing image...</span>
		</center>
	{/if}

	<br />
</main>

<style>
	main {
		text-align: center;
		align-content: center;
		padding: 10px;
	}

	input {
		width: 240px;
	}

	h1 {
		font-size: 40px;
		background-color: #1dd3b0;
		color: white;
		width: 300px;
	}

	span {
		font-size: 16px;
	}

	#result {
		max-width: 30vw;
		min-width: 240px;
		height: auto;
	}

	#icon {
		width: 55px;
		height: 55px;
		object-fit: contain;
		padding-bottom: 0px;
		padding-top: 10px;
	}

	.man-img {
		max-width: 30%;
		min-width: 240px;
		height: auto;
		border-width: 0.5px;
		border-style: solid;
		padding: 1px;
		border-radius: 5px;
		background-color: black;
	}

	.header {
		flex-direction: row;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.loader {
		border: 16px solid #f3f3f3; /* Light grey */
		border-top: 16px solid #1dd3b0; /* Blue */
		border-radius: 50%;
		width: 120px;
		height: 120px;
		animation: spin 2s linear infinite;
	}

	@keyframes spin {
		0% {
			transform: rotate(0deg);
		}
		100% {
			transform: rotate(360deg);
		}
	}
</style>
