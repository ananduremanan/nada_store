<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { Avatar } from 'flowbite-svelte';
	import {
		ShoppingBagSolid,
		UserRemoveSolid,
		ArrowLeftToBracketOutline,
		CartPlusAltSolid
	} from 'flowbite-svelte-icons';

	const hash = $page.url.searchParams.get('id');

	let avatrImgUrl: string;
	let userEmail: string;
	let userName: string;
	let isAdmin: boolean;

	const getUserImage = async () => {
		let user = localStorage.getItem('user');
		if (user) {
			avatrImgUrl = `https://gravatar.com/avatar/${hash}?s=200`;
			userEmail = JSON.parse(user).email;
			isAdmin = JSON.parse(user).isAdmin;
			let splitEmail = userEmail.split('@');
			userName = splitEmail[0];
		}
	};

	onMount(() => {
		getUserImage();
	});
</script>

<section class="flex flex-col items-center mt-8">
	<Avatar src={avatrImgUrl} size={'xl'} />
	<div class="mt-8">{userName}</div>
	<div class="text-sm">{userEmail}</div>

	<div class="border border-gray-500 rounded-lg w-full p-2 mt-4 flex flex-col gap-2">
		{#if isAdmin}
			<div class="flex gap-2"><CartPlusAltSolid />Add New Products Package</div>
		{/if}
		<div class="flex gap-2"><ShoppingBagSolid />My Purchases</div>
		<div class="flex gap-2"><ArrowLeftToBracketOutline />Logout</div>
		<div class="flex gap-2"><UserRemoveSolid />Delete Account</div>
	</div>
</section>
