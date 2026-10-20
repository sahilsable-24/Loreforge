import { Plus } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <div className="mx-auto max-w-6xl px-4 py-12">
      <p className="eyebrow">Your guild</p>
      <h1 className="mt-2 text-4xl">Campaigns</h1>

      <section className="mt-12 rounded-xl border border-border bg-card px-6 py-12 text-center">
        <h2 className="text-2xl">Start your first campaign</h2>
        <p className="mx-auto mt-2 max-w-md text-muted-foreground text-balance">
          A campaign holds your party, your rulebooks and your world lore.
        </p>
        <Button className="mt-6">
          <Plus aria-hidden="true" />
          New campaign
        </Button>
      </section>
    </div>
  );
}