<script lang="ts">
	import { Card, Button, Rating, Badge } from 'flowbite-svelte';
	import { Carousel } from 'flowbite-svelte';

	const images = [
		{
			alt: 'VR VPN',
			src: '/images/VR_VPN.svg',
			title: 'sergey-pesterev-tMvuB9se2uQ-unsplash'
		},
		{
			alt: 'Sergey Pesterev',
			src: '/images/VR_WORLD.svg',
			title: 'sergey-pesterev-tMvuB9se2uQ-unsplash'
		}
	];
</script>

<section>
	<Carousel {images} duration={3000} />
	<div class="mb-8 text-base">Hot In Wearables</div>
	<div class="grid grid-cols-2 gap-2 md:grid-cols-4 md:gap-4">
		<Card>
			<img src="https://flowbite-svelte.com/images/product-1.webp" alt="" />
			<h2 class="font-bold">Apple Watch Series 3</h2>
			<Rating rating={3} size={18} class="mt-2" />
			<div class="w-full flex justify-between items-center mt-2">
				<h3 class="text-sm">399 SUD</h3>
				<Button class="text-xs p-1 bg-black dark:bg-white dark:text-black md:text-base"
					>Buy Now</Button
				>
			</div>
		</Card>
		<Card>
			<img src="https://flowbite-svelte.com/images/product-1.webp" alt="" />
			<h2 class="font-bold">Apple Watch Series 3</h2>
			<Rating rating={3} size={18} class="mt-2" />
			<div class="w-full flex justify-between items-center mt-2">
				<h3 class="text-sm">399 SUD</h3>
				<Button class="text-xs p-1 bg-black dark:bg-white dark:text-black md:text-base"
					>Buy Now</Button
				>
			</div>
		</Card>
		<Card>
			<img src="https://flowbite-svelte.com/images/product-1.webp" alt="" />
			<h2 class="font-bold">Apple Watch Series 3</h2>
			<Rating rating={3} size={18} class="mt-2" />
			<div class="w-full flex justify-between items-center mt-2">
				<h3 class="text-sm">399 SUD</h3>
				<Button class="text-xs p-1 bg-black dark:bg-white dark:text-black md:text-base"
					>Buy Now</Button
				>
			</div>
		</Card>
		<Card>
			<img src="https://flowbite-svelte.com/images/product-1.webp" alt="" />
			<h2 class="font-bold">Apple Watch Series 3</h2>
			<Rating rating={3} size={18} class="mt-2" />
			<div class="w-full flex justify-between items-center mt-2">
				<h3 class="text-sm">399 SUD</h3>
				<Button class="text-xs p-1 bg-black dark:bg-white dark:text-black md:text-base"
					>Buy Now</Button
				>
			</div>
		</Card>
	</div>
</section>
