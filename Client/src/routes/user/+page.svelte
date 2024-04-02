<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { Avatar } from 'flowbite-svelte';
	import { Separator } from 'bits-ui';

	const hash = $page.url.searchParams.get('id');

	let avatrImgUrl: string;
	let userEmail: string;
	let userName: string;

	const getUserImage = async () => {
		let user = localStorage.getItem('user');
		if (user) {
			avatrImgUrl = `https://gravatar.com/avatar/${hash}?s=200`;
			userEmail = JSON.parse(user).email;
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

	<div class="border border-gray-500 rounded-lg w-full p-2 mt-4">
		<div>My Purchases</div>
	</div>
</section>
