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


class AtandtIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "atandt"

    @property
    def original_file_name(self) -> "str":
        return "atandt.svg"

    @property
    def title(self) -> "str":
        return "AT&T"

    @property
    def primary_color(self) -> "str":
        return "#009FDB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AT&amp;T</title>
     <path d="M4.584 21.438a12.077 12.077 0 0 0 7.349 2.495 12 12 0 0
 0 7.887-2.967c-.944.607-3.64 2.023-7.887 2.023-3.708
 0-6.068-.81-7.349-1.55m8.158.606c2.966 0 6.202-.809
 8.09-2.427.539-.405 1.01-1.011
 1.483-1.753.27-.472.539-1.011.741-1.483-1.82 2.63-7.011 4.315-12.404
 4.315-3.776 0-7.888-1.214-9.506-3.573 1.483 3.236 6 4.92 11.596
 4.92m-3.236-5.257C3.37 16.787.472 13.955 0 12c0 .674.067 1.483.202
 2.09.068.27.27.674.607 1.079 1.483 1.55 5.191 3.707 11.595 3.707
 8.697 0 10.72-2.898
 11.124-3.842.27-.674.472-1.888.472-2.967v-.674c-.607 2.292-8.022
 5.394-14.494 5.394m-8.427-9.91C.742 7.55.337 8.763.202 9.37c-.067.27
 0 .404.068.607.741 1.55 4.45 4.044 13.078 4.044 5.259 0 9.371-1.28
 10.045-3.64.135-.404.135-.876
 0-1.483-.202-.674-.472-1.483-.809-2.09.068 3.101-8.562 5.124-12.944
 5.124-4.719
 0-8.696-1.888-8.696-4.248.067-.337.135-.606.135-.809M19.82
 3.034c.068.067.068.135.068.27 0 1.348-4.045 3.64-10.517 3.64-4.787
 0-5.663-1.753-5.663-2.9 0-.404.135-.808.472-1.213-.607.607-1.146
 1.147-1.686 1.82-.202.27-.337.54-.337.675 0 2.36 5.865 3.977 11.259
 3.977 5.797 0 8.427-1.887 8.427-3.573
 0-.606-.203-.943-.81-1.618a17.301 17.301 0 0
 0-1.213-1.078m-1.753-1.281A11.794 11.794 0 0 0 11.933.067C9.64.067
 7.55.674 5.73 1.82c-.539.27-.876.54-.876.877 0 1.01 2.36 2.09 6.54
 2.09 4.112 0 7.348-1.214 7.348-2.36.067-.202-.203-.405-.675-.674" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
