"use client";

import { useState } from "react";

const terms = ["First Term", "Second Term", "Third Term"];

export default function ParentDashboard() {
  const [children, setChildren] = useState<any[]>([
    { name: "John Doe", school: "ABC Primary School", grade: "Primary 3" },
    { name: "Jane Doe", school: "XYZ Secondary School", grade: "JSS 1" },
  ]);

  const [selectedChild, setSelectedChild] = useState<any | null>(null);
  const [selectedTerms, setSelectedTerms] = useState<string[]>([]);

  const [childForm, setChildForm] = useState({
    name: "",
    school: "",
    grade: "",
  });

  const handleAddChild = () => {
    if (!childForm.name || !childForm.school || !childForm.grade) {
      alert("Please fill in all fields to add a child.");
      return;
    }

    setChildren([...children, childForm]);
    setChildForm({ name: "", school: "", grade: "" }); // Reset form
  };

  const handleApplyForFee = () => {
    if (!selectedChild) {
      alert("Please select a child.");
      return;
    }

    if (selectedTerms.length === 0) {
      alert("Please select at least one term.");
      return;
    }

    alert(
      `Application submitted for ${selectedChild.name} for the following terms: ${selectedTerms.join(
        ", "
      )}.`
    );

    // Reset form after submission
    setSelectedChild(null);
    setSelectedTerms([]);
  };

  const handleTermToggle = (term: string) => {
    setSelectedTerms((prev) =>
      prev.includes(term)
        ? prev.filter((t) => t !== term)
        : [...prev, term]
    );
  };

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Sidebar */}
      <aside className="w-64 bg-gray-800 text-gray-100">
        <div className="p-4 text-center text-xl font-semibold border-b border-gray-700">
          Parent Dashboard
        </div>
        <nav className="p-4">
          <ul className="space-y-2">
            <li className="flex items-center gap-4 p-3 rounded-md cursor-pointer hover:bg-gray-700 hover:text-white">
              <span>👨‍👩‍👦</span>
              <span>Children</span>
            </li>
            <li className="flex items-center gap-4 p-3 rounded-md cursor-pointer hover:bg-gray-700 hover:text-white">
              <span>💰</span>
              <span>Apply for School Fee</span>
            </li>
          </ul>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-8">
        <h1 className="text-3xl font-bold mb-6 text-gray-800">
          Welcome to the Parent Dashboard
        </h1>

        {/* Children Section */}
        <div className="mb-8">
          <h2 className="text-2xl font-semibold mb-4 text-gray-800">Your Children</h2>
          {children.length === 0 ? (
            <div className="bg-white p-6 rounded-lg shadow">
              <p className="text-gray-700 mb-4">You have no children added yet.</p>
              <button
                onClick={() => document.getElementById("addChildModal")?.click()}
                className="bg-indigo-600 text-white py-2 px-4 rounded hover:bg-indigo-700"
              >
                Add a Child
              </button>
            </div>
          ) : (
            <div className="bg-white p-6 rounded-lg shadow">
              <table className="w-full border-collapse border border-gray-300">
                <thead>
                  <tr className="bg-gray-200">
                    <th className="border border-gray-300 px-4 py-2 text-gray-700">
                      Name
                    </th>
                    <th className="border border-gray-300 px-4 py-2 text-gray-700">
                      School
                    </th>
                    <th className="border border-gray-300 px-4 py-2 text-gray-700">
                      Grade
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {children.map((child, index) => (
                    <tr key={index} className="hover:bg-gray-100">
                      <td className="border border-gray-300 px-4 py-2 text-gray-800">
                        {child.name}
                      </td>
                      <td className="border border-gray-300 px-4 py-2 text-gray-800">
                        {child.school}
                      </td>
                      <td className="border border-gray-300 px-4 py-2 text-gray-800">
                        {child.grade}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>

        {/* Apply for School Fee */}
        <div className="mb-8">
          <h2 className="text-2xl font-semibold mb-4 text-gray-800">Apply for School Fee</h2>
          <div className="bg-white p-6 rounded-lg shadow">
            <div className="mb-4">
              <label className="block mb-2 text-gray-700">Select Child *</label>
              <select
                value={selectedChild ? selectedChild.name : ""}
                onChange={(e) =>
                  setSelectedChild(children.find((child) => child.name === e.target.value))
                }
                className="w-full rounded-md border border-gray-300 p-2"
              >
                <option value="">Select a child</option>
                {children.map((child, index) => (
                  <option key={index} value={child.name}>
                    {child.name} - {child.school}
                  </option>
                ))}
              </select>
            </div>

            <div className="mb-4">
              <label className="block mb-2 text-gray-700">Select Terms *</label>
              <div className="flex gap-4">
                {terms.map((term) => (
                  <label key={term} className="flex items-center space-x-2">
                    <input
                      type="checkbox"
                      checked={selectedTerms.includes(term)}
                      onChange={() => handleTermToggle(term)}
                      className="h-5 w-5 text-indigo-600"
                    />
                    <span>{term}</span>
                  </label>
                ))}
              </div>
            </div>

            <button
              onClick={handleApplyForFee}
              className="bg-indigo-600 text-white py-2 px-4 rounded hover:bg-indigo-700"
            >
              Submit Application
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}
