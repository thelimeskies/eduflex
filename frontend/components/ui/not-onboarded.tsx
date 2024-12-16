// "use client";

// import { useState } from "react";

// export default function NotOnboarded({ username }: { username: string }) {
//   const [selectedRole, setSelectedRole] = useState<string | null>(null);

//   const handleSelection = (role: string) => {
//     setSelectedRole(role);
//     console.log(`Selected Role: ${role}`);
//     // Add navigation logic or API call here
//   };

//   const handleLogout = () => {
//     console.log("Logging out...");
//     // Replace with logout logic
//   };

//   return (
//     <div className="flex h-screen items-center justify-center bg-gray-900 text-gray-200">
//       <div className="max-w-lg rounded-lg bg-gray-800 p-8 shadow-lg">
//         <h2 className="text-center text-3xl font-semibold mb-6">
//           Welcome, {username}
//         </h2>
//         <p className="text-center mb-6 text-indigo-200/70">
//           Please select your role to continue.
//         </p>

//         <div className="space-y-4">
//           <button
//             onClick={() => handleSelection("parent")}
//             className="w-full rounded-md bg-indigo-600 py-3 text-lg font-medium text-white shadow hover:bg-indigo-700"
//           >
//             Proceed as a Parent
//           </button>

//           <button
//             onClick={() => handleSelection("school")}
//             className="w-full rounded-md bg-indigo-500 py-3 text-lg font-medium text-white shadow hover:bg-indigo-600"
//           >
//             Proceed as a School
//           </button>
//         </div>

//         {selectedRole && (
//           <div className="mt-6 text-center">
//             <p className="text-indigo-300">
//               You have selected:{" "}
//               <span className="font-medium text-white capitalize">
//                 {selectedRole}
//               </span>
//             </p>
//           </div>
//         )}

//         <div className="mt-8 text-center">
//           <button
//             onClick={handleLogout}
//             className="inline-block rounded-md border border-red-500 px-6 py-2 text-sm font-medium text-red-500 transition hover:bg-red-500 hover:text-white"
//           >
//             Logout
//           </button>
//         </div>
//       </div>
//     </div>
//   );
// }


"use client";

import { useState } from "react";

export default function NotOnboarded({ username = "Guest" }: { username?: string }) {
  const [selectedRole, setSelectedRole] = useState<string | null>(null);

  const handleSelection = (role: string) => {
    setSelectedRole(role);
    console.log(`Selected Role: ${role}`);
  };

  const handleLogout = () => {
    console.log("Logging out...");
  };

  return (
    <div className="flex h-screen items-center justify-center bg-gray-900 text-gray-200">
      <div className="max-w-lg rounded-lg bg-gray-800 p-8 shadow-lg">
        <h2 className="text-center text-3xl font-semibold mb-6">
          Welcome, {username}
        </h2>
        <p className="text-center mb-6 text-indigo-200/70">
          Please select your role to continue.
        </p>

        <div className="space-y-4">
          <button
            onClick={() => handleSelection("parent")}
            className="w-full rounded-md bg-indigo-600 py-3 text-lg font-medium text-white shadow hover:bg-indigo-700"
          >
            Proceed as a Parent
          </button>

          <button
            onClick={() => handleSelection("school")}
            className="w-full rounded-md bg-indigo-500 py-3 text-lg font-medium text-white shadow hover:bg-indigo-600"
          >
            Proceed as a School
          </button>
        </div>

        {selectedRole && (
          <div className="mt-6 text-center">
            <p className="text-indigo-300">
              You have selected:{" "}
              <span className="font-medium text-white capitalize">
                {selectedRole}
              </span>
            </p>
          </div>
        )}

        <div className="mt-8 text-center">
          <button
            onClick={handleLogout}
            className="inline-block rounded-md border border-red-500 px-6 py-2 text-sm font-medium text-red-500 transition hover:bg-red-500 hover:text-white"
          >
            Logout
          </button>
        </div>
      </div>
    </div>
  );
}
