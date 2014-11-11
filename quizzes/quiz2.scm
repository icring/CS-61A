; CS 61A Fall 2014
; Name: Sony Theakanath
; Login: cs61a-ach

(define (assert-equal value expression)
  (if (equal? value (eval expression))
    (print 'ok)
    (print (list 'for expression ':
                 'expected value
                 'but 'got (eval expression)))))

; Utility functions
(define (add-two x) (+ x 2))
(define (square x) (* x x))
(define (cadr s) (car (cdr s)))

(define (equal-answer f1 f2)
  ; YOUR CODE HERE
  (lambda (x) (if (= (f1 x) (f2 x))
                  #t
                  #f)))

(define (test-equal-answer)
  (print (list 'testing 'equal-answer))
  ; (add-two 2) evaluates to 4, (square 2) also evaluates to 4
  (assert-equal true  '((equal-answer add-two square) 2))
  ; (add-two 3) evaluates to 5, (square 3) instead evaluates to 9
  (assert-equal false '((equal-answer add-two square) 3))

  )

(test-equal-answer)

(define (num-adjacent-matches s)
  (cond ((= 1 (length s)) 0)
        ((= (car s) (cadr s)) (+ 1 (num-adjacent-matches (cdr s))))
        (else (num-adjacent-matches (cdr s)))
  ))

(define (test-num-adjacent-matches)
  (print (list 'testing 'num-adjacent-matches))
  ; no pairs
  (assert-equal 0 '(num-adjacent-matches '(1 2 3 4)))
  ; one pair of 1's
  (assert-equal 1 '(num-adjacent-matches '(1 1 2 3)))
  ; one pair of 1's, one pair of 2's
  (assert-equal 2 '(num-adjacent-matches '(1 1 2 2)))
  ; three pairs of 1's
  (assert-equal 3 '(num-adjacent-matches '(1 1 1 1)))

  )

(test-num-adjacent-matches)

(define (in-dict dict item) 
   (cond ((= 0 (length dict)) #f)
         ((eq? (car (car dict)) item) #t)
         (else (in-dict (cdr dict) item))
   )
)

(define (acc dict item) 
   (if (eq? (car (car dict)) item)
       (cons (cons (car (car dict)) (+ 1 (cdr (car dict)))) (cdr dict))
       (cons (car dict) (acc (cdr dict) item))
   )
)

(define (tally names)
  (define (tally-helper names current-dict)
     (cond ((= 0 (length names)) current-dict)
           ((in-dict current-dict (car names)) (tally-helper (cdr names) (acc current-dict (car names))))
           (else (tally-helper (cdr names) (append current-dict (cons (cons (car names) 1) nil))))
     )
  )
  (tally-helper names ())
)

(define (test-tally)
  (print (list 'testing 'tally))
  (assert-equal '((obama . 1))
                '(tally '(obama)))
  (assert-equal '((taft . 3))
                '(tally '(taft taft taft)))
  (assert-equal '((jerry . 2) (brown . 1))
                '(tally '(jerry jerry brown)))
  (assert-equal '((jane . 5) (jack . 2) (jill . 1))
                '(tally '(jane jack jane jane jack jill jane jane)))
  (assert-equal '((jane . 5) (jack . 2) (jill . 1))
                '(tally '(jane jack jane jane jill jane jane jack)))

  )



(test-tally)

