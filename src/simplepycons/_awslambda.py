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


class AwsLambdaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "awslambda"

    @property
    def original_file_name(self) -> "str":
        return "awslambda.svg"

    @property
    def title(self) -> "str":
        return "AWS Lambda"

    @property
    def primary_color(self) -> "str":
        return "#FF9900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AWS Lambda</title>
     <path d="M4.9855 0c-.2941.0031-.5335.2466-.534.5482L4.446 5.456c0
 .1451.06.2835.159.3891a.5322.5322 0 0 0 .3806.1562h3.4282l8.197
 17.6805a.5365.5365 0 0 0 .4885.3181h5.811c.2969 0
 .5426-.2448.5426-.5482V18.544c0-.3035-.2392-.5482-.5425-.5482h-2.0138L12.7394.3153C12.647.124
 12.4564 0 12.2452 0h-7.254Zm.5397 1.0907h6.3678l8.16
 17.6804a.5365.5365 0 0 0 .4885.3181h1.8178v3.8173H17.437L9.2402
 5.226a.536.536 0 0 0-.4885-.318H5.5223Zm2.0137
 8.2366c-.2098.0011-.3937.1193-.4857.3096L.6002 23.2133a.5506.5506 0 0
 0 .0313.5282.5334.5334 0 0 0 .4544.25h6.169a.5468.5468 0 0 0
 .497-.3096l3.38-7.166a.5405.5405 0 0 0-.0029-.4686L8.036
 9.637a.5468.5468 0 0 0-.4942-.3096Zm.0057 1.8036 2.488 5.1522-3.1214
 6.6206H1.9465Z" />
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
