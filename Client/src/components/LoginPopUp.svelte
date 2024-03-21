<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	let userName: string;
	let password: string;

	const dispatch = createEventDispatcher();

	function cancel() {
		dispatch('cancel', false);
	}

	const handleLogin = async () => {
		const reponse = fetch('http://127.0.0.1:5000/api/login');
	};
</script>

<div
	class="z-10 bg-black text-white p-4 rounded-xl flex flex-col gap-5 w-full m-8 justify-center items-center relative"
>
	<button
		class="bg-white text-black w-6 h-6 rounded-full text-center absolute top-1 right-1"
		on:click={cancel}>x</button
	>
	<img src="/images/login.webp" alt="login bot" width="200" />
	<div class="text-2xl">Login To Access Your Account</div>
	<input
		type="text"
		placeholder="Enter Your Email"
		class="p-2 w-full rounded-md outline-0 text-black text-xl"
		bind:value={userName}
	/>
	<input
		type="password"
		placeholder="Enter Your Password"
		class="p-2 w-full rounded-md outline-0 text-black text-xl"
		bind:value={password}
	/>
	<button
		class="bg-white text-black p-2 rounded-md w-full text-xl"
		on:click={() => {
			console.log(userName, password);
		}}>Login</button
	>
</div>
