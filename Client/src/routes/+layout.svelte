<script lang="ts">
	import '../app.css';
	import LoginPopUp from '../components/LoginPopUp.svelte';
	import { onMount } from 'svelte';
	import md5 from 'md5';

	let isOpen: boolean = false;
	let avatrImgUrl: string;

	onMount(() => {
		const getUserImage = async (email: string) => {
			if (email != '') {
				const normalizedEmail = typeof email === 'string' ? email.trim().toLowerCase() : '';
				const hash = md5(normalizedEmail);
				avatrImgUrl = `https://gravatar.com/avatar/${hash}?s=200`;
			}
		};

		let user = localStorage.getItem('user');
		if (user) {
			let parsedUserData = JSON.parse(user);
			getUserImage(parsedUserData.email);
		}
	});
</script>

<nav class="px-8 lg:px-28 py-4 flex justify-between sticky top-0 z-50 bg-white">
	<a href="/" class="text-lg">Nada Store</a>
	<div>
		{#if avatrImgUrl != undefined}
			<img src={avatrImgUrl} alt="{avatrImgUrl} avatar" class="w-10 h-10 rounded-xl" />
		{:else}
			<button
				class="bg-black text-white px-2 py-1 rounded-md"
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
			<LoginPopUp on:cancel={(event) => (isOpen = event.detail)} />
		</div>
	{/if}
</main>
