#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class FilezillaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "filezilla"

    @property
    def original_file_name(self) -> "str":
        return "filezilla.svg"

    @property
    def title(self) -> "str":
        return "FileZilla"

    @property
    def primary_color(self) -> "str":
        return "#BF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FileZilla</title>
     <path d="M23.999 1.861V.803a.81.81 0 0 1-.568-.236.81.81 0 0
 1-.234-.567h-1.06a.806.806 0 0 1-1.608 0h-1.06a.805.805 0 0 1-1.608
 0h-1.059a.807.807 0 0 1-.845.765.808.808 0 0
 1-.764-.765h-1.06a.806.806 0 0 1-1.609 0h-1.058a.805.805 0 0 1-1.608
 0h-1.06a.794.794 0 0 1-.825.774A.803.803 0 0 1 7.197 0h-1.06A.806.806
 0 0 1 4.53 0H3.47a.803.803 0 0 1-1.607 0H.803a.806.806 0 0
 1-.802.803V1.86a.804.804 0 0 1 0 1.607v1.06a.803.803 0 0 1 0
 1.607v1.059a.805.805 0 0 1 0 1.608v1.06a.803.803 0 1 1 0
 1.607v1.06a.803.803 0 0 1 0 1.606v1.06a.803.803 0 1 1 0
 1.608v1.06c.444.017.79.388.774.83a.801.801 0 0
 1-.774.775v1.061a.803.803 0 1 1 0 1.608v1.06A.805.805 0 0 1 .804
 24h1.06a.806.806 0 0 1 1.607 0h1.06a.806.806 0 0 1 1.608
 0h1.059a.806.806 0 0 1 1.609 0h1.06a.804.804 0 0 1 1.607
 0h1.06a.806.806 0 0 1 1.607 0H15.2a.807.807 0 0 1 1.61
 0h1.058a.807.807 0 0 1 1.61 0h1.059a.804.804 0 0 1 1.606
 0h1.054c0-.21.086-.418.235-.568a.808.808 0 0 1
 .567-.234v-1.06a.805.805 0 0 1 0-1.606v-1.06a.805.805 0 0 1
 0-1.608v-1.06a.806.806 0 0 1 0-1.608v-1.061a.804.804 0 0 1
 0-1.608V11.47a.806.806 0 0 1 0-1.608v-1.06a.804.804 0 0 1
 0-1.607v-1.06a.805.805 0 0 1 0-1.606v-1.06a.806.806 0 0 1
 0-1.608zm-4.067 9.836L13.53 17.92c.58.09 1.14.225 1.742.225 1.464 0
 3.147-.445 4.285-.916l-.584 2.745c-1.675.805-2.7.87-3.701.87-1.095
 0-2.144-.356-3.215-.356-.602 0-1.473.045-2.008.4l-1.16-2.052
 6.604-6.54h-7.6l-1.45 6.806h-3.17L6.577 3.528h10.487l-.67
 3.145H9.097l-.624 2.924h11.973z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:FileZ'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
