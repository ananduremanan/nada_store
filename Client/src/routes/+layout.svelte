<script lang="ts">
	import '../app.css';
	import LoginPopUp from '../components/LoginPopUp.svelte';
	import { onMount } from 'svelte';
	import md5 from 'md5';
	import { DarkMode } from 'flowbite-svelte';
	import { page } from '$app/stores';

	const isLoggedIn = $page.url.searchParams.has('id');

	let isOpen: boolean = false;
	let avatrImgUrl: string;
	let hash: string;

	const getUserImage = async () => {
		let user = localStorage.getItem('user');
		if (user) {
			let parsedUserData = JSON.parse(user);
			const normalizedEmail =
				typeof parsedUserData.email === 'string' ? parsedUserData.email.trim().toLowerCase() : '';
			hash = md5(normalizedEmail);
			avatrImgUrl = `https://gravatar.com/avatar/${hash}?s=200`;
		}
	};

	onMount(() => {
		getUserImage();
	});
</script>

<nav class="px-8 lg:px-28 py-4 flex justify-between sticky top-0 z-50 bg-white dark:bg-black">
	<a href="/" class="text-lg">Nada Store</a>
	<div class="flex items-center justify-center gap-4">
		<DarkMode class="text-black dark:text-white hover:bg-white dark:hover:bg-black" />
		{#if avatrImgUrl != undefined}
			<a href="/user?id={hash}"
				><img src={avatrImgUrl} alt="{avatrImgUrl} avatar" class="w-10 h-10 rounded-xl" /></a
			>
		{:else}
			<button
				class="bg-black text-white px-2 py-1 rounded-md dark:bg-white dark:text-black"
				on:click={() => {
					isOpen = !isOpen;
				}}>Login</button
			>
		{/if}
	</div>
</nav>

<main class="px-8 lg:px-28 relative">
	<slot />
	{#if isOpen}
		<div class="fixed inset-0 flex justify-center items-center z-50">
			<LoginPopUp
				on:cancel={(event) => {
					isOpen = event.detail;
					getUserImage();
				}}
			/>
		</div>
	{/if}
</main>
