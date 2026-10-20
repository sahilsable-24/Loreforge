import type { Metadata } from "next";
import { Source_Serif_4, IBM_Plex_Sans } from "next/font/google";
import "./globals.css";

const serif = Source_Serif_4({
  subsets: ["latin"],
  variable: "--font-source-serif",
});

const sans = IBM_Plex_Sans({
  subsets: ["latin"],
  weight: ["400", "500"],
  variable: "--font-plex-sans",
});

export const metadata: Metadata = {
  title: "Loreforge",
  description: "An AI game master for your tabletop group.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang="en"
      className={`${serif.variable} ${sans.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">
        <header className="bg-topbar border-b border-border">
          <div className="mx-auto flex h-14 max-w-6xl items-center px-4">
            <span className="font-serif text-xl font-semibold text-topbar-foreground">
              Loreforge<span className="text-topbar-accent">.</span>
            </span>
          </div>
        </header>
        <main className="flex-1">{children}</main>
      </body>
    </html>
  );
}