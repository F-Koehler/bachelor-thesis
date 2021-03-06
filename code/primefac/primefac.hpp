#ifndef PRIMEFAC_HPP_
#define PRIMEFAC_HPP_

#include "config.hpp"
#include "threading.hpp"
#include "sieve.hpp"
#include <utility>
#include <chrono>
#include <fstream>

namespace primefac
{
	typedef struct {
		std::size_t N;
		std::size_t Nc;
		std::size_t Na;
		double Fc;
		double kB;
	} PrimefacParameters;

	typedef struct {
		bool success;
		std::pair<std::size_t, std::size_t> factors;
		std::size_t usedSteps;
		std::chrono::microseconds duration;
	} PrimefacResult;

	typedef struct {
		std::size_t N1;
		std::size_t N2;
		std::size_t Nc;
		std::size_t Na;
		double Fc;
		double kB;
	} SemiprimeParameters;

	typedef struct {
		bool success;
		std::pair<std::size_t, std::size_t> factors;
		std::size_t usedNa;
		std::chrono::microseconds duration;
	} SemiprimeResult;

	PrimefacResult factorize(const PrimefacParameters& parameters);
	PrimefacResult factorize(const PrimefacParameters& parameters, std::size_t numThreads);
	SemiprimeResult factorizeSemiprime(const SemiprimeParameters& parameters);
	SemiprimeResult factorizeSemiprime(const SemiprimeParameters& parameters, std::size_t numThreads);

	std::ostream& operator<<(std::ostream& out, const PrimefacResult& r);
	std::ostream& operator<<(std::ostream& out, const SemiprimeResult& r);

	std::ostream& operator<<(std::ostream& out, const PrimefacParameters& p);
	std::ostream& operator<<(std::ostream& out, const SemiprimeParameters& p);

	std::ofstream& operator<<(std::ofstream& out, const PrimefacParameters& p);
	std::ofstream& operator<<(std::ofstream& out, const SemiprimeParameters& p);
}

#endif
