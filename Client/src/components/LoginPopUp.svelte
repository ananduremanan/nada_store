<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import notify from '../components/Notify.svelte';

	let email: string;
	let password: string;
	let loading: boolean = false;
	let loginError: boolean = false;

	const dispatch = createEventDispatcher();

	function cancel() {
		dispatch('cancel', false);
	}

	const handleLogin = async () => {
		try {
			loading = true;
			const response = await fetch('http://127.0.0.1:5000/api/login', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					email: email,
					password: password
				})
			});
			const data = await response.json();
			if (data.status === 'success') {
				localStorage.setItem('user', JSON.stringify(data));
			} else {
				loginError = true;
				notify(true, 'Error', 'Error');
			}
		} catch (error) {
			console.error(error);
		} finally {
			loading = false;
		}
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
		bind:value={email}
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
			handleLogin();
		}}
	>
		{#if loading}
			Please Wait...
		{:else}
			Login
		{/if}
	</button>
	<div>
		Don't Have An Account ? <a href="/signup" on:click={cancel}
			><span class="underline decoration-dashed">Sign Up</span></a
		>
	</div>
</div>
