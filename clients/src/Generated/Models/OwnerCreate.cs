// <auto-generated/>

#nullable disable

using System;
using System.Collections.Generic;
using PetStore;

namespace PetStore.Models
{
    /// <summary> Resource create operation model. </summary>
    public partial class OwnerCreate
    {
        /// <summary> Keeps track of any properties unknown to the library. </summary>
        private protected readonly IDictionary<string, BinaryData> _additionalBinaryDataProperties;

        /// <summary> Initializes a new instance of <see cref="OwnerCreate"/>. </summary>
        /// <param name="name"></param>
        /// <param name="age"></param>
        /// <exception cref="ArgumentNullException"> <paramref name="name"/> is null. </exception>
        public OwnerCreate(string name, int age)
        {
            Argument.AssertNotNull(name, nameof(name));

            Name = name;
            Age = age;
        }

        internal OwnerCreate(string name, int age, IDictionary<string, BinaryData> additionalBinaryDataProperties)
        {
            Name = name;
            Age = age;
            _additionalBinaryDataProperties = additionalBinaryDataProperties;
        }

        /// <summary> Gets the Name. </summary>
        public string Name { get; }

        /// <summary> Gets the Age. </summary>
        public int Age { get; }
    }
}
