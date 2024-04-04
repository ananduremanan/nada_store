<script lang="ts">
	import { Card, Button, Rating, Badge } from 'flowbite-svelte';
	import { Carousel } from 'flowbite-svelte';
</script>

<section>
	<div class="mb-4 text-base">Hot In Templates</div>
	<div class="grid grid-cols-1 gap-2 md:grid-cols-4 md:gap-4">
		<Card padding={'none'} class="rounded-3xl">
			<img src="/images/svelte.svg" alt="" />
			<div class="p-4 lg:p-6">
				<h2 class="font-bold">Svelte E-Commerce Web Template</h2>
				<Rating rating={3} size={18} class="mt-2" />
				<div class="w-full flex justify-between items-center mt-2">
					<h3 class="text-sm">399 SUD</h3>
					<Button class="text-xs p-1 bg-black dark:bg-white dark:text-black md:text-base"
						>Buy Now</Button
					>
				</div>
			</div>
		</Card>
		<Card padding={'none'} class="rounded-3xl">
			<img src="/images/SwiftUI.png" alt="" class="object-cover" />
			<div class="p-4 lg:p-6">
				<h2 class="font-bold">SwiftUI Component Library</h2>
				<Rating rating={4.5} size={18} class="mt-2" />
				<div class="w-full flex justify-between items-center mt-2">
					<h3 class="text-sm">699 SUD</h3>
					<Button class="text-xs p-1 bg-black dark:bg-white dark:text-black md:text-base"
						>Buy Now</Button
					>
				</div>
			</div>
		</Card>
		<Card padding={'none'} class="rounded-3xl">
			<img src="/images/svelte.svg" alt="" />
			<div class="p-4 lg:p-6">
				<h2 class="font-bold">Svelte E-Commerce Web Template</h2>
				<Rating rating={3} size={18} class="mt-2" />
				<div class="w-full flex justify-between items-center mt-2">
					<h3 class="text-sm">399 SUD</h3>
					<Button class="text-xs p-1 bg-black dark:bg-white dark:text-black md:text-base"
						>Buy Now</Button
					>
				</div>
			</div>
		</Card>
	</div>
</section>
