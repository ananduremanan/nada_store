<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import { postSET } from '$lib';
	import { Button } from 'flowbite-svelte';
	import { Spinner } from 'flowbite-svelte';

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
			loginError = false;
			const res = await postSET({
				destination: 'http://127.0.0.1:5000/api/login',
				body: { email: email, password: password }
			});
			if (res.status === 'success') {
				loginError = false;
				localStorage.setItem('user', JSON.stringify(res));
				cancel();
			} else {
				loginError = true;
			}
		} catch (error) {
			console.error(error);
		} finally {
			loading = false;
		}
	};
</script>

<div
	class="z-10 bg-black text-white p-4 rounded-xl flex flex-col gap-5 w-full m-8 justify-center items-center relative md:w-96 dark:bg-gray-900"
>
	<button
		class="bg-white text-black w-6 h-6 rounded-full text-center absolute top-1 right-1"
		on:click={cancel}>x</button
	>
	<img src="/images/login.webp" alt="login bot" width="200" />
	<div class="text-2xl md:text-lg">Login To Access Your Account</div>
	<input
		type="text"
		placeholder="Enter Your Email"
		class="p-2 w-full rounded-md outline-0 text-black text-xl md:text-lg"
		bind:value={email}
		required
	/>
	<input
		type="password"
		placeholder="Enter Your Password"
		class="p-2 w-full rounded-md outline-0 text-black text-xl md:text-lg"
		bind:value={password}
		required
	/>
	{#if loginError}
		<div class="text-xs">Wrong User Email or Password</div>
	{/if}
	<Button
		color="alternative"
		class="bg-white text-black p-2 rounded-md w-full text-xl md:text-lg"
		on:click={() => {
			handleLogin();
		}}
		>{#if loading}
			<Spinner size="4" />Please Wait...
		{:else}
			Login
		{/if}</Button
	>

	<div>
		Don't Have An Account ? <a href="/signup" on:click={cancel}
			><span class="underline decoration-dashed">Sign Up</span></a
		>
	</div>
</div>
