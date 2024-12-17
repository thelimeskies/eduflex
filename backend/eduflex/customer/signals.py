from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from customer.models import Parents, ParentKYC, ParentCreditCapacityScore
import random


@receiver(post_save, sender=ParentKYC)
def calculate_credit_capacity_score(sender, instance, created, **kwargs):
    if created:
        if settings.RUN_SIMULATION:
            # Simulate realistic credit and capacity score scenarios
            case_a = {
                "credit_score": random.randint(75, 85),
                "capacity_score": random.randint(70, 80),
                "credit_score_description": "Good",
                "capacity_score_description": "Stable Income, Low Expenses",
                "credit_score_recommendation": (
                    "Your financial habits are commendable, and your credit score reflects "
                    "that. Maintain timely payments on any existing debts, avoid taking on "
                    "unnecessary loans, and continue building a solid credit history. "
                    "Consider small investments to further grow your wealth."
                ),
                "capacity_score_recommendation": (
                    "You are managing your income and expenses well. To maintain this trend, "
                    "continue budgeting effectively, prioritize savings, and avoid lifestyle inflation. "
                    "With your stable income, you can comfortably manage additional loans."
                ),
            }
            case_b = {
                "credit_score": random.randint(50, 65),
                "capacity_score": random.randint(45, 55),
                "credit_score_description": "Average",
                "capacity_score_description": "Moderate Income, Moderate Expenses",
                "credit_score_recommendation": (
                    "Your credit score is fair, but there's room for improvement. Focus on "
                    "making consistent and on-time repayments to boost your score. Reduce "
                    "credit card usage and avoid opening multiple credit accounts simultaneously."
                ),
                "capacity_score_recommendation": (
                    "Your financial capacity is currently balanced, but unexpected expenses could "
                    "cause strain. Review your expenses and identify areas to cut back. Consider setting "
                    "up an emergency fund to improve your financial security."
                ),
            }
            case_c = {
                "credit_score": random.randint(20, 40),
                "capacity_score": random.randint(30, 45),
                "credit_score_description": "Poor",
                "capacity_score_description": "Low Income, High Expenses",
                "credit_score_recommendation": (
                    "Your credit score indicates significant financial stress. Prioritize paying off "
                    "high-interest debts as soon as possible. Avoid taking on new loans and seek financial "
                    "counseling to create a debt repayment plan. Focus on rebuilding your credit gradually."
                ),
                "capacity_score_recommendation": (
                    "Your expenses are currently too high relative to your income. It is critical to reassess "
                    "your spending habits and prioritize essentials. Look for opportunities to increase your "
                    "income, such as additional work or freelance projects, to improve your capacity."
                ),
            }
            case_d = {
                "credit_score": random.randint(85, 95),
                "capacity_score": random.randint(85, 95),
                "credit_score_description": "Excellent",
                "capacity_score_description": "High Income, Strong Savings",
                "credit_score_recommendation": (
                    "You have an excellent credit history, which makes you eligible for premium financial products. "
                    "Continue maintaining this score by managing your credit wisely and ensuring all payments are made on time. "
                    "Consider exploring investment opportunities or premium credit options with favorable rates."
                ),
                "capacity_score_recommendation": (
                    "With a strong income and savings capacity, you are in a position to achieve significant financial milestones. "
                    "Consider long-term financial goals, such as purchasing property, saving for education, or planning for retirement. "
                    "Continue managing your expenses responsibly to sustain this capacity."
                ),
            }
            case_e = {
                "credit_score": random.randint(60, 75),
                "capacity_score": random.randint(55, 65),
                "credit_score_description": "Fair",
                "capacity_score_description": "Stable Income, Moderate Savings",
                "credit_score_recommendation": (
                    "Your credit score is fair, indicating good financial habits with some minor issues. "
                    "To improve further, prioritize clearing smaller debts first, avoid late payments, and limit credit usage. "
                    "Regularly monitor your credit report for accuracy."
                ),
                "capacity_score_recommendation": (
                    "You have a stable financial foundation, but there’s room to build a stronger savings buffer. "
                    "Focus on growing your savings, reducing discretionary spending, and planning for unforeseen expenses. "
                    "With careful planning, you can handle additional financial responsibilities comfortably."
                ),
            }
            case_f = {
                "credit_score": random.randint(35, 50),
                "capacity_score": random.randint(40, 50),
                "credit_score_description": "Low",
                "capacity_score_description": "Unstable Income, Low Savings",
                "credit_score_recommendation": (
                    "Your credit score suggests financial instability. It’s essential to minimize borrowing and prioritize debt repayment. "
                    "Seek financial advice to consolidate debts and reduce high-interest liabilities. Start rebuilding your credit one step at a time."
                ),
                "capacity_score_recommendation": (
                    "Your financial capacity needs improvement. Focus on stabilizing your income sources and building consistent savings. "
                    "Identify and eliminate unnecessary expenses to free up more cash flow and improve your financial resilience."
                ),
            }
            case_g = {
                "credit_score": random.randint(75, 85),
                "capacity_score": random.randint(25, 40),
                "credit_score_description": "Good Credit, Poor Capacity",
                "capacity_score_description": "High Debt Relative to Income",
                "credit_score_recommendation": (
                    "Your credit score is strong, but you’re at risk due to poor financial capacity. "
                    "Avoid taking on additional loans until your existing debts are reduced. Focus on timely repayments to maintain your good credit score."
                ),
                "capacity_score_recommendation": (
                    "Your current financial obligations exceed your income capacity. Prioritize paying down debts with the highest interest rates, "
                    "and consider increasing your income to regain financial balance."
                ),
            }
            case_h = {
                "credit_score": random.randint(40, 60),
                "capacity_score": random.randint(70, 85),
                "credit_score_description": "Average Credit, Strong Capacity",
                "capacity_score_description": "Healthy Income, Low Debt",
                "credit_score_recommendation": (
                    "Your credit score is average but improving. Focus on consistent, on-time payments, and avoid maxing out credit limits. "
                    "With a strong financial capacity, you can gradually rebuild your credit."
                ),
                "capacity_score_recommendation": (
                    "Your strong capacity score reflects a healthy financial situation. Use this stability to strategically plan for large expenses, "
                    "build investments, or explore additional credit options with favorable terms."
                ),
            }

            # Randomly select one case for simulation
            simulated_case = random.choice(
                [case_a, case_b, case_c, case_d, case_e, case_f, case_g, case_h]
            )

            # Create or update the credit capacity score for the parent
            ParentCreditCapacityScore.objects.create(
                parent=instance.parent,
                credit_score=simulated_case["credit_score"],
                capacity_score=simulated_case["capacity_score"],
                credit_score_description=simulated_case["credit_score_description"],
                capacity_score_description=simulated_case["capacity_score_description"],
                credit_score_recommendation=simulated_case[
                    "credit_score_recommendation"
                ],
                capacity_score_recommendation=simulated_case[
                    "capacity_score_recommendation"
                ],
            )
