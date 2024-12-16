"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

const menuItems = [
  { name: "Dashboard", icon: "🏠", key: "dashboard" },
  { name: "Students", icon: "👩‍🎓", key: "students" },
  { name: "Fee Collection", icon: "💰", key: "fees" },
  { name: "Notifications", icon: "🔔", key: "notifications" },
  { name: "Settings", icon: "⚙️", key: "settings" },
];

export default function SchoolDashboard() {
  const [activeTab, setActiveTab] = useState("dashboard");
  const router = useRouter();

  const handleNavigation = (key: string) => {
    setActiveTab(key);
    // You can add routing if needed
    console.log("Navigating to:", key);
  };

  const renderContent = () => {
    switch (activeTab) {
      case "dashboard":
        return (
          <div>
            <h2 className="text-2xl font-semibold mb-4">Welcome to Your Dashboard</h2>
            <p>Here you can manage your school activities and view key metrics.</p>
          </div>
        );
      case "students":
        return (
          <div>
            <h2 className="text-2xl font-semibold mb-4">Manage Students</h2>
            <p>View and manage your student records, admissions, and more.</p>
          </div>
        );
      case "fees":
        return (
          <div>
            <h2 className="text-2xl font-semibold mb-4">Fee Collection</h2>
            <p>Track fee payments and generate invoices for parents.</p>
          </div>
        );
      case "notifications":
        return (
          <div>
            <h2 className="text-2xl font-semibold mb-4">Notifications</h2>
            <p>View and manage notifications sent to parents and staff.</p>
          </div>
        );
      case "settings":
        return (
          <div>
            <h2 className="text-2xl font-semibold mb-4">Settings</h2>
            <p>Update your school details, preferences, and more.</p>
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-gray-800 text-gray-200">
        <div className="p-4 text-center text-xl font-semibold border-b border-gray-700">
          School Dashboard
        </div>
        <nav className="p-4">
          <ul className="space-y-2">
            {menuItems.map((item) => (
              <li
                key={item.key}
                onClick={() => handleNavigation(item.key)}
                className={`flex items-center gap-4 p-3 rounded-md cursor-pointer ${
                  activeTab === item.key
                    ? "bg-indigo-600 text-white"
                    : "hover:bg-gray-700 hover:text-white"
                }`}
              >
                <span>{item.icon}</span>
                <span>{item.name}</span>
              </li>
            ))}
          </ul>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-8">
        <div className="mb-6">
          <h1 className="text-3xl font-bold">School Dashboard</h1>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-lg">{renderContent()}</div>
      </main>
    </div>
  );
}
