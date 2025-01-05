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


class JhipsterIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jhipster"

    @property
    def original_file_name(self) -> "str":
        return "jhipster.svg"

    @property
    def title(self) -> "str":
        return "JHipster"

    @property
    def primary_color(self) -> "str":
        return "#3E8ACC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JHipster</title>
     <path d="M20.709 7.171c-2.455-.029-6.332 1.749-8.684
 2.962-3.434-1.75-10.178-4.729-10.942-1.54-1.03 4.297-2.187 7.563.985
 8.167 2.207.42 7.122-2.43 9.912-4.205 2.78 1.771 7.746 4.66 9.96
 4.231 3.168-.616 2-3.896.961-8.208-.24-1-1.067-1.394-2.192-1.407z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/jhipster/jhipster-artwork/
blob/1085d85ab6d819b9ef7f6cc710ec8a4977b95e90/logos/JHipster%20bowtie.'''

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
