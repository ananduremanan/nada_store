<script lang="ts">
	import '../../app.css';
</script>

<section class="relative flex flex-col items-center">
	<img src="/images/signup.png" alt="signup" width="200" class="z-0 relative" />
	<div>SignUp To Use Nada Store</div>
	<div class="flex flex-col gap-2 w-full mt-4 md:w-96">
		<input
			type="email"
			placeholder="Enter Your Email"
			class="p-2 w-full rounded-md text-black text-sm outline-1 outline-dotted"
		/>
		<input
			type="text"
			placeholder="Enter Your User Name"
			class="p-2 w-full rounded-md text-black text-sm outline-1 outline-dotted"
		/>
		<input
			type="password"
			placeholder="Enter Your Password"
			class="p-2 w-full rounded-md text-black text-sm outline-1 outline-dotted"
		/>
		<input
			type="password"
			placeholder="Confirm Password"
			class="p-2 w-full rounded-md text-black text-sm outline-1 outline-dotted"
		/>
		<input
			type="phone"
			placeholder="Enter Your Phone"
			class="p-2 w-full rounded-md text-black text-sm outline-1 outline-dotted"
		/>
		<textarea
			placeholder="Enter Your Address"
			class="p-2 w-full rounded-md text-black text-sm outline-1 outline-dotted"
			rows="5"
		/>
		<div class="text-xs">By Signing Up you're agreeing to our terms and conditions.</div>
		<button class="bg-black text-white p-2 rounded-md w-full text-sm mb-8" on:click={() => {}}
			>Sign Up</button
		>
	</div>
</section>
