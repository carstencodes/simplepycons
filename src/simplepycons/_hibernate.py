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


class HibernateIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hibernate"

    @property
    def original_file_name(self) -> "str":
        return "hibernate.svg"

    @property
    def title(self) -> "str":
        return "Hibernate"

    @property
    def primary_color(self) -> "str":
        return "#59666C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hibernate</title>
     <path d="M5.365 0L9.98 7.994h8.95L14.31 0H5.366zm-.431.248L.46
 7.994l4.613 8.008L9.55 8.24 4.934.248zm13.992 7.75l-4.475 7.76 4.617
 7.992 4.471-7.744-4.613-8.008zm-4.905 8.006l-8.95.002L9.688
 24h8.946l-4.615-7.994.001-.002Z" />
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
