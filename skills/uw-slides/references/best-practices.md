# Presentation Best Practices

Distilled from UW-Madison Strategic Communications' "Slide Presentations the StratComm Way" guide. These rules govern content generation.

## Content Rules

1. **Sharpen the title.** Keep it brief. Use a call to action, invite curiosity, or use numbers. "Six Ways We Made Badgers for Life" beats "Improvement of Student Retention through the Leadership Initiative Pilot Program."

2. **Less is more.** Simplify and limit words on each slide. Text-heavy slides are boring, hard to follow, and steal attention from the speaker. Slides reinforce your words; they do not replace them.

3. **Bigger is better.** No text smaller than 24pt equivalent. For accessibility and readability on projectors and small screens alike.

4. **Mind your case.** No all-capital-letter headings. Title case and sentence case are more accessible and readable.

5. **Keep it clean.** No distracting patterns underneath text. Avoid text on images without sufficient contrast. Never put black text on a red background.

6. **Stick to brand fonts.** Red Hat Display for headings, Red Hat Text for body. Arial as fallback. No decorative or novelty fonts.

7. **Skip the gimmicks.** No flashy slide transitions. If animations are used, they must serve a purpose (guiding audience attention, revealing information progressively). Entrance animations should be subtle (fade, slide-up).

8. **Don't be a teleprompter.** Slide content is for the audience, not the speaker. Put detailed notes in the presenter notes (data-notes attribute), not on the slide face.

9. **Consider small screens.** Remote viewers may see slides on phones or tablets. Responsive design (clamp, viewport units) handles this, but avoid layouts that break below 600px width.

## Structural Rules

10. **8-15 slides is the sweet spot.** Fewer feels thin; more risks losing the audience. Split into sections of 3-5 slides each.

11. **One idea per slide.** If a slide tries to make two points, split it into two slides.

12. **Use section dividers.** Break the presentation into 2-4 major sections with red divider slides. This provides visual rhythm and helps the audience track progress.

13. **Start strong, end clear.** Title slide should intrigue. Closing slide should have contact info or a call to action, not just "Thank You."

14. **Data needs context.** Charts and numbers need a clear heading that states the takeaway, not just the topic. "Revenue Grew 23%" is better than "Revenue Data."

## Accessibility Rules

15. **Spell out acronyms on first use.** "Retrieval-Augmented Generation (RAG)" on first mention; "RAG" thereafter. Aids comprehension for non-experts and accessibility for screen reader users. Per UW IT accessible presentations guidance.

16. **Use plain language.** Avoid jargon when a common word will do. Define technical terms in context when the audience may not know them. Per UW IT accessible presentations guidance.

17. **Write meaningful presenter notes.** Every slide with a chart, image, diagram, code block, or non-trivial visual layout needs a `data-notes="..."` attribute describing what the visual shows and why it matters. Someone reading only the notes (without seeing the slide) should understand the content. Per UW Policy UW-519 and UW IT accessibility guidance.
