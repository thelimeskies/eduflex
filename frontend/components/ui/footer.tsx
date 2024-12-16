import Logo from "./logo";
import Image from "next/image";
import FooterIllustration from "@/public/images/footer-illustration.svg";

export default function Footer() {
  return (
    <footer className="relative bg-gray-900 py-12 md:py-16">
      {/* Footer Illustration */}
      <div
        className="pointer-events-none absolute bottom-0 left-1/2 -z-10 -translate-x-1/2 opacity-50"
        aria-hidden="true"
      >
        <Image
          className="max-w-none"
          src={FooterIllustration}
          width={1076}
          height={378}
          alt="Footer illustration"
        />
      </div>

      {/* Footer Content */}
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <div className="grid grid-cols-2 gap-8 md:grid-cols-4 lg:grid-cols-[repeat(4,minmax(0,200px))_1fr]">
          {/* 1st Block: About EduFlex */}
          <div>
            <div className="mb-3">
              <Logo />
            </div>
            <p className="text-sm text-indigo-200/70">
              EduFlex provides innovative solutions for school fee payments,
              empowering both parents and schools with financial flexibility.
            </p>
          </div>

          {/* 2nd Block: Company */}
          <div>
            <h3 className="text-sm font-medium text-gray-200 mb-2">Company</h3>
            <ul className="space-y-2 text-sm">
              <li>
                <a className="text-indigo-200/70 hover:text-indigo-500" href="/about">
                  About Us
                </a>
              </li>
              <li>
                <a className="text-indigo-200/70 hover:text-indigo-500" href="/careers">
                  Careers
                </a>
              </li>
              <li>
                <a className="text-indigo-200/70 hover:text-indigo-500" href="/blog">
                  Blog
                </a>
              </li>
            </ul>
          </div>

          {/* 3rd Block: Resources */}
          <div>
            <h3 className="text-sm font-medium text-gray-200 mb-2">Resources</h3>
            <ul className="space-y-2 text-sm">
              <li>
                <a className="text-indigo-200/70 hover:text-indigo-500" href="/faq">
                  FAQs
                </a>
              </li>
              <li>
                <a
                  className="text-indigo-200/70 hover:text-indigo-500"
                  href="/contact"
                >
                  Contact Support
                </a>
              </li>
              <li>
                <a
                  className="text-indigo-200/70 hover:text-indigo-500"
                  href="/terms"
                >
                  Terms of Service
                </a>
              </li>
            </ul>
          </div>

          {/* 4th Block: Social Media */}
          <div>
            <h3 className="text-sm font-medium text-gray-200 mb-2">Connect</h3>
            <ul className="flex gap-3">
              <li>
                <a
                  className="text-indigo-500 hover:text-indigo-400"
                  href="https://twitter.com"
                  aria-label="Twitter"
                >
                  <svg
                    className="h-6 w-6 fill-current"
                    viewBox="0 0 32 32"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path d="m13.063 9 3.495 4.475L20.601 9h2.454l-5.359 5.931L24 23h-4.938l-3.866-4.893L10.771 23H8.316l5.735-6.342L8 9h5.063Z" />
                  </svg>
                </a>
              </li>
              <li>
                <a
                  className="text-indigo-500 hover:text-indigo-400"
                  href="https://facebook.com"
                  aria-label="Facebook"
                >
                  <svg
                    className="h-6 w-6 fill-current"
                    viewBox="0 0 32 32"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path d="M18 8h4V2h-6a6 6 0 0 0-6 6v4H6v6h4v12h6V18h4l2-6h-6V8Z" />
                  </svg>
                </a>
              </li>
              <li>
                <a
                  className="text-indigo-500 hover:text-indigo-400"
                  href="https://linkedin.com"
                  aria-label="LinkedIn"
                >
                  <svg
                    className="h-6 w-6 fill-current"
                    viewBox="0 0 32 32"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path d="M4 4h6v6H4V4Zm2 10h4v14H6V14Zm8 0h4v2h.1a4.5 4.5 0 0 1 4-2c3 0 5 2 5 5v9h-4v-8c0-2-1-3-3-3s-3 1-3 3v8h-4V14Z" />
                  </svg>
                </a>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom Section */}
        <div className="mt-8 border-t border-gray-700 pt-6 text-center text-sm text-indigo-200/70">
          <p>
            © {new Date().getFullYear()} EduFlex. All rights reserved.{" "}
            <a href="/privacy" className="hover:text-indigo-500">
              Privacy Policy
            </a>
          </p>
        </div>
      </div>
    </footer>
  );
}
